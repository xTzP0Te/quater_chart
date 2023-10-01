import flet as ft
# import cmath
import numpy as np


def main(page: ft.Page):
    page.title = "Решалка для квадратных уравнений + рисовалка графиков"

    a_field = ft.Ref[ft.TextField]()
    b_field = ft.Ref[ft.TextField]()
    c_field = ft.Ref[ft.TextField]()

    size_label_text = 40
    size_axis_text = 20

    data = [
        ft.LineChartData(
            data_points=[
                # ft.LineChartDataPoint(-15, 15),
                # ft.LineChartDataPoint(-11, 13),
                # ft.LineChartDataPoint(-3, 11),
                # ft.LineChartDataPoint(-2, -14),
                # ft.LineChartDataPoint(-1, 11),
                # ft.LineChartDataPoint(0, 13),
                # ft.LineChartDataPoint(4, 15),
                # ft.LineChartDataPoint(12, 16),

            ],
            stroke_width=2,
            color=ft.colors.AMBER,
            curved=True,
            stroke_cap_round=True,
        )
    ]

    chart = ft.LineChart(
        data_series=data,
        animate=True,
        border=ft.Border(
            bottom=ft.BorderSide(4, ft.colors.with_opacity(0.5, ft.colors.ON_SURFACE))
        ),
        left_axis=ft.ChartAxis(
            labels=[
                ft.ChartAxisLabel(
                    value=-20,
                    label=ft.Text("-20", size=size_axis_text, weight=ft.FontWeight.BOLD)
                ),
                ft.ChartAxisLabel(
                    value=-10,
                    label=ft.Text("-10", size=size_axis_text, weight=ft.FontWeight.BOLD)
                ),
                ft.ChartAxisLabel(
                    value=0,
                    label=ft.Text("0", size=size_axis_text, weight=ft.FontWeight.BOLD)
                ),
                ft.ChartAxisLabel(
                    value=10,
                    label=ft.Text("10", size=size_axis_text, weight=ft.FontWeight.BOLD)
                ),
                ft.ChartAxisLabel(
                    value=20,
                    label=ft.Text("20", size=size_axis_text, weight=ft.FontWeight.BOLD)
                ),
            ]
        ),
        bottom_axis=ft.ChartAxis(
            labels=[
                ft.ChartAxisLabel(
                    value=-20,
                    label=ft.Text("-20", size=size_axis_text, weight=ft.FontWeight.BOLD)
                ),
                ft.ChartAxisLabel(
                    value=-10,
                    label=ft.Text("-10", size=size_axis_text, weight=ft.FontWeight.BOLD)
                ),
                ft.ChartAxisLabel(
                    value=0,
                    label=ft.Text("0", size=size_axis_text, weight=ft.FontWeight.BOLD)
                ),
                ft.ChartAxisLabel(
                    value=10,
                    label=ft.Text("10", size=size_axis_text, weight=ft.FontWeight.BOLD)
                ),
                ft.ChartAxisLabel(
                    value=20,
                    label=ft.Text("20", size=size_axis_text, weight=ft.FontWeight.BOLD)
                ),
            ]
        )
    )

    result_row = [
        ft.DataTable(
                    columns=[
                        ft.DataColumn(ft.Text("Корни")),
                        ft.DataColumn(ft.Text("Значения")),
                    ],
                    rows=[
                        ft.DataRow(
                            cells=[
                                ft.DataCell(ft.Text("X1")),
                                ft.DataCell(ft.Text("?")),
                            ],
                        ),
                        ft.DataRow(
                            cells=[
                                ft.DataCell(ft.Text("X2")),
                                ft.DataCell(ft.Text("?")),
                            ],
                        ),
                    ],
                ),
        ]

    def cal_roots(e):
        print("call func cal_root")
        a = float(a_field.current.value)
        b = float(b_field.current.value)
        c = float(c_field.current.value)

        # # Вычислите дискриминант
        # d = cmath.sqrt(b ** 2 - 4 * a * c)
        #
        # # Вычислите корни
        # x1 = (-b + d) / (2 * a)
        # x2 = (-b - d) / (2 * a)
        d = b * b - 4 * a * c
        x1 = (-b + np.sqrt(d)) / (2 * a)
        x2 = (-b - np.sqrt(d)) / (2 * a)
        print(x1, x2)

        result_row[0].rows[0].cells[1] = ft.DataCell(ft.Text(str(x1)))
        result_row[0].rows[1].cells[1] = ft.DataCell(ft.Text(str(x2)))

        # print(type(result_row[0].rows[0].cells[0]))
        # print(result_row[0].rows[0].cells[1].content)

        for i in range(-5,6):
            data[0].data_points.append(ft.LineChartDataPoint(i, a * i ** 2 + b * i + c))

        page.update()

    page.add(
        ft.Row(
            [
                ft.Container(
                    content=ft.TextField(ref=a_field, label="a", autofocus=True, max_length=3, value='1')
                    # content=ft.Text("Non clickable"),
                    # margin=10,
                    # padding=10,
                    # alignment=ft.alignment.center,
                    # bgcolor=ft.colors.AMBER,
                    # width=150,
                    # height=150,
                    # border_radius=10,
                ),
                ft.Container(
                    content=ft.Text("x^2 + ", size=size_label_text),
                    # content=ft.Text("Clickable without Ink"),
                    # margin=10,
                    # padding=10,
                    # alignment=ft.alignment.center,
                    # bgcolor=ft.colors.GREEN_200,
                    # width=150,
                    # height=150,
                    # border_radius=10,
                    # on_click=lambda e: print("Clickable without Ink clicked!"),
                ),
                ft.Container(
                    content=ft.TextField(ref=b_field, label="b", max_length=3, value='4')
                    # content=ft.Text("Clickable with Ink"),
                    # margin=10,
                    # padding=10,
                    # alignment=ft.alignment.center,
                    # bgcolor=ft.colors.CYAN_200,
                    # width=150,
                    # height=150,
                    # border_radius=10,
                    # ink=True,
                    # on_click=lambda e: print("Clickable with Ink clicked!"),
                ),
                ft.Container(
                    content=ft.Text("x + ", size=size_label_text),
                    # content=ft.Text("Clickable transparent with Ink"),
                    # margin=10,
                    # padding=10,
                    # alignment=ft.alignment.center,
                    # width=150,
                    # height=150,
                    # border_radius=10,
                    # ink=True,
                    # on_click=lambda e: print("Clickable transparent with Ink clicked!"),
                ),
                ft.Container(
                    content=ft.TextField(ref=c_field, label="c", max_length=3, value='3')
                ),
                ft.Container(
                    content=ft.Text(" = 0 ", size=size_label_text),
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.ElevatedButton("Решить", on_click=cal_roots),
        ft.Row(
            result_row,
            # [
                # ft.DataTable(
                #     columns=[
                #         ft.DataColumn(ft.Text("Корни")),
                #         ft.DataColumn(ft.Text("Значения")),
                #     ],
                #     rows=[
                #         ft.DataRow(
                #             cells=[
                #                 ft.DataCell(ft.Text("X1")),
                #                 ft.DataCell(ft.Text("14")),
                #             ],
                #         ),
                #         ft.DataRow(
                #             cells=[
                #                 ft.DataCell(ft.Text("X2")),
                #                 ft.DataCell(ft.Text("5")),
                #             ],
                #         ),
                #     ],
                # ),

            # ]
        ),
        chart,
        # ft.Row(
        #     [
        #         chart,
        #     ]
        # )

    )


# if _name_ == '_main_':
ft.app(target=main)
