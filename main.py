import pandas as pd
from config import DB_URI
from charts_generation import create_bar_2x1, create_hist_2x2
from sqlalchemy import create_engine


engine = create_engine(DB_URI)

with engine.connect() as conn:

    query = """
        SELECT c.customer_id, c.first_name, c.last_name, c.country, i.total
        FROM customer AS c
        INNER JOIN invoice AS i
        ON c.customer_id = i.customer_id
        ORDER BY customer_id, total DESC
    """
    
    df = pd.read_sql(query, conn)
    data = df.groupby('customer_id')['total'].agg(['mean', 'max', 'min', 'median'])

    create_hist_2x2(
        first_values=data['median'],
        second_values=data['min'],
        third_values=data['mean'],
        fourth_values=data['max'],
        first_title='median',
        second_title='min',
        third_title='mean',
        fourth_title='max',
        filename='invoice_stats_mean_median_min_max'
    )

    total_from_country = df.groupby('country')['total'].max()
    first_data = df.groupby('country')['total'].sum()


    create_bar_2x1(
        first_categories=first_data.index,
        first_values=first_data.values,
        first_title='Сумма покупок клиентов по странам',
        first_yname='Общая выручка',
        first_rotation=45,
        first_ha='right',
        
        second_categories=total_from_country.index,
        second_values=total_from_country.values,
        second_title='Распределение максимальной суммы покупки клиента по странам',
        second_xname='Страны',
        second_yname='Максимальный чек одной покупки',
        second_rotation=45,
        second_ha='right',
        filename='revenue_and_max_check_by_country'
    )

    names = df.drop_duplicates('customer_id').set_index('customer_id')['first_name']
    top_clients = df.groupby('customer_id')['total'].sum().nlargest(7)
    top_names = names.loc[top_clients.index].values
    top_single_purchases = df.nlargest(7, 'total')
    

    create_bar_2x1(
        first_categories=top_single_purchases['first_name'],
        first_values=top_single_purchases['total'],
        first_title='Клиенты совершившие самые большие разовые покупки',
        first_yname='Сумма покупки',
        
        second_categories=top_names,
        second_values=top_clients.values,
        second_title='Топ клиентов по объему выручки',
        second_xname='Имена клиентов',
        second_yname='Общая сумма покупок',
        filename='top_purchases_and_clients_by_revenue'
    )