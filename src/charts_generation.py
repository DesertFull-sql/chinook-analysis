import matplotlib.pyplot as plt
from config import IMAGES_DIR


def create_hist_2x2(
    first_values,
    second_values,
    third_values,
    fourth_values,
    first_title: str = None,
    second_title: str = None,
    third_title: str = None,
    fourth_title: str = None,
    bins: int = 20,
    filename: str = 'two_histograms'
):
    """
    Построить 4 гистограммы.

    Args:
        first_values: Данные для 1 гистограммы.
        second_values: Данные для 2 гистограммы.
        third_values: Данные для 3 гистограммы.
        fourth_values: Данные для 4 гистограммы.
        first_title: Заголовок 1 гистограммы.
        second_title: Заголовок 2 гистограммы.
        third_title: Заголовок 3 гистограммы.
        fourth_title: Заголовок 4 гистограммы.
        bins: Количество интервалов.
        filename: Название Гистограммы.
    """
    _ , axes = plt.subplots(2, 2)

    axes[0, 0].hist(first_values, bins=bins)
    axes[0, 0].set_title(first_title)

    axes[0, 1].hist(second_values, bins=bins)
    axes[0, 1].set_title(second_title)

    axes[1, 0].hist(third_values, bins=bins)
    axes[1, 0].set_title(third_title)

    axes[1, 1].hist(fourth_values, bins=bins)
    axes[1, 1].set_title(fourth_title)
    
    plt.tight_layout()
    plt.savefig(IMAGES_DIR / filename)
    


def create_bar_2x1(
    first_categories,
    first_values,
    second_categories,
    second_values,
    first_title: str = None,
    second_title: str = None,
    first_xname: str = None,
    second_xname: str = None,
    first_yname: str = None,
    second_yname: str = None,
    first_rotation: int = 0,
    second_rotation: int = 0,
    first_ha: str = 'center',
    second_ha: str = 'center',
    xsize: int = 10, 
    ysize: int = 8,
    filename: str = 'four_diagram'
    ):
    """
    Построить 2 диаграммы.

    Args:
        first_categories: Категории по оси X первой диаграммы.
        first_values: Категории по оси Y первой диаграммы.
        second_categories: Категории по оси X второй диаграммы.
        second_values: Категории по оси Y второй диаграммы.
        first_title: Заголовок 1 диаграммы.
        second_title: Заголовок 2 диаграммы.
        first_xname: Подпись по оси X первой диаграммы.
        second_xname: Подпись по оси X второй диаграммы.
        first_yname: Подпись по оси Y первой диаграммы.
        second_yname: Подпись по оси Y второй диаграммы.
        first_rotation: Угол поворота подписей оси X первой диаграммы.
        second_rotation: Угол поворота подписей оси X второй диаграммы.
        first_ha: Выравнивание подписей первой диаграммы.
        second_ha: Выравнивание подписей второй диаграммы.
        xsize: Ширина фигуры.
        ysize: Высота фигуры.
        filename: Название Диаграммы.
    """
    _ , axes = plt.subplots(2, 1, figsize=(xsize, ysize))

    axes[0].bar(first_categories, first_values)
    axes[0].set_title(first_title)
    axes[0].set_xlabel(first_xname)
    axes[0].set_ylabel(first_yname)
    axes[0].set_xticks(
        first_categories,
        labels=first_categories,
        rotation=first_rotation,
        ha=first_ha
    )

    axes[1].bar(second_categories, second_values)
    axes[1].set_title(second_title)
    axes[1].set_xlabel(second_xname)
    axes[1].set_ylabel(second_yname)
    axes[1].set_xticks(
        second_categories,
        labels=second_categories,
        rotation=second_rotation,
        ha=second_ha
    )

    plt.tight_layout()
    plt.savefig(IMAGES_DIR / filename)