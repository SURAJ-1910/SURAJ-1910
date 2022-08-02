{
  "cells": [
    {
      "cell_type": "code",
      "source": [
        "import numpy  as np\n",
        "import pandas as pd\n",
        "import seaborn as sns\n",
        "import matplotlib.pyplot as plt"
      ],
      "metadata": {
        "id": "1z7OTCsVlPnr"
      },
      "execution_count": 1,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Importing a data frame"
      ],
      "metadata": {
        "id": "Cb2V5_bgMScr"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "df = pd.read_csv(\"/content/House_rental.csv\")\n",
        "df.head()"
      ],
      "metadata": {
        "id": "RDYxZL3clPl3",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "outputId": "dbe29229-53f2-4df0-b434-2dee2b8df2a5"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "   Unnamed: 0      Sqft  Floor  TotalFloor  Bedroom  Living.Room  Bathroom  \\\n",
              "0           1  1177.698      2           7        2            2         2   \n",
              "1           2  2134.800      5           7        4            2         2   \n",
              "2           3  1138.560      5           7        2            2         1   \n",
              "3           4  1458.780      2           7        3            2         2   \n",
              "4           5   967.776     11          14        3            2         2   \n",
              "\n",
              "   Price  \n",
              "0  62000  \n",
              "1  78000  \n",
              "2  58000  \n",
              "3  45000  \n",
              "4  45000  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-23d383d2-2e33-4f03-9204-59874b4064af\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Unnamed: 0</th>\n",
              "      <th>Sqft</th>\n",
              "      <th>Floor</th>\n",
              "      <th>TotalFloor</th>\n",
              "      <th>Bedroom</th>\n",
              "      <th>Living.Room</th>\n",
              "      <th>Bathroom</th>\n",
              "      <th>Price</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1</td>\n",
              "      <td>1177.698</td>\n",
              "      <td>2</td>\n",
              "      <td>7</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>62000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>2</td>\n",
              "      <td>2134.800</td>\n",
              "      <td>5</td>\n",
              "      <td>7</td>\n",
              "      <td>4</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>78000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>3</td>\n",
              "      <td>1138.560</td>\n",
              "      <td>5</td>\n",
              "      <td>7</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>1</td>\n",
              "      <td>58000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>4</td>\n",
              "      <td>1458.780</td>\n",
              "      <td>2</td>\n",
              "      <td>7</td>\n",
              "      <td>3</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>45000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>5</td>\n",
              "      <td>967.776</td>\n",
              "      <td>11</td>\n",
              "      <td>14</td>\n",
              "      <td>3</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>45000</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-23d383d2-2e33-4f03-9204-59874b4064af')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-23d383d2-2e33-4f03-9204-59874b4064af button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-23d383d2-2e33-4f03-9204-59874b4064af');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 5
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df.info()"
      ],
      "metadata": {
        "id": "UuDuoujilPkW",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "8b57b23c-e63b-4426-93eb-2227d22602fe"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 645 entries, 0 to 644\n",
            "Data columns (total 8 columns):\n",
            " #   Column       Non-Null Count  Dtype  \n",
            "---  ------       --------------  -----  \n",
            " 0   Unnamed: 0   645 non-null    int64  \n",
            " 1   Sqft         645 non-null    float64\n",
            " 2   Floor        645 non-null    int64  \n",
            " 3   TotalFloor   645 non-null    int64  \n",
            " 4   Bedroom      645 non-null    int64  \n",
            " 5   Living.Room  645 non-null    int64  \n",
            " 6   Bathroom     645 non-null    int64  \n",
            " 7   Price        645 non-null    int64  \n",
            "dtypes: float64(1), int64(7)\n",
            "memory usage: 40.4 KB\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df.describe()"
      ],
      "metadata": {
        "id": "3QAdAKWGlPjg",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 382
        },
        "outputId": "976ebeee-a41a-4456-a750-841e058a4038"
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "       Unnamed: 0         Sqft       Floor  TotalFloor     Bedroom  \\\n",
              "count  645.000000   645.000000  645.000000  645.000000  645.000000   \n",
              "mean   325.159690  1527.656260    5.939535   10.855814    2.837209   \n",
              "std    187.312152   767.386531    3.884721    4.996208    1.010740   \n",
              "min      1.000000   359.358000    1.000000    1.000000    1.000000   \n",
              "25%    164.000000   925.080000    3.000000    7.000000    2.000000   \n",
              "50%    326.000000  1423.200000    5.000000   12.000000    3.000000   \n",
              "75%    487.000000  1892.856000    8.000000   14.000000    4.000000   \n",
              "max    648.000000  5856.468000   22.000000   38.000000    7.000000   \n",
              "\n",
              "       Living.Room    Bathroom          Price  \n",
              "count   645.000000  645.000000     645.000000  \n",
              "mean      1.813953    1.810853   61986.823256  \n",
              "std       0.462364    0.683574   35635.091007  \n",
              "min       0.000000    0.000000    6100.000000  \n",
              "25%       2.000000    1.000000   39000.000000  \n",
              "50%       2.000000    2.000000   50000.000000  \n",
              "75%       2.000000    2.000000   75000.000000  \n",
              "max       4.000000    5.000000  250000.000000  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-0addc8c9-1af6-49b1-931b-71a65f442e50\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Unnamed: 0</th>\n",
              "      <th>Sqft</th>\n",
              "      <th>Floor</th>\n",
              "      <th>TotalFloor</th>\n",
              "      <th>Bedroom</th>\n",
              "      <th>Living.Room</th>\n",
              "      <th>Bathroom</th>\n",
              "      <th>Price</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>count</th>\n",
              "      <td>645.000000</td>\n",
              "      <td>645.000000</td>\n",
              "      <td>645.000000</td>\n",
              "      <td>645.000000</td>\n",
              "      <td>645.000000</td>\n",
              "      <td>645.000000</td>\n",
              "      <td>645.000000</td>\n",
              "      <td>645.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>mean</th>\n",
              "      <td>325.159690</td>\n",
              "      <td>1527.656260</td>\n",
              "      <td>5.939535</td>\n",
              "      <td>10.855814</td>\n",
              "      <td>2.837209</td>\n",
              "      <td>1.813953</td>\n",
              "      <td>1.810853</td>\n",
              "      <td>61986.823256</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>std</th>\n",
              "      <td>187.312152</td>\n",
              "      <td>767.386531</td>\n",
              "      <td>3.884721</td>\n",
              "      <td>4.996208</td>\n",
              "      <td>1.010740</td>\n",
              "      <td>0.462364</td>\n",
              "      <td>0.683574</td>\n",
              "      <td>35635.091007</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>min</th>\n",
              "      <td>1.000000</td>\n",
              "      <td>359.358000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>6100.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>25%</th>\n",
              "      <td>164.000000</td>\n",
              "      <td>925.080000</td>\n",
              "      <td>3.000000</td>\n",
              "      <td>7.000000</td>\n",
              "      <td>2.000000</td>\n",
              "      <td>2.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>39000.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>50%</th>\n",
              "      <td>326.000000</td>\n",
              "      <td>1423.200000</td>\n",
              "      <td>5.000000</td>\n",
              "      <td>12.000000</td>\n",
              "      <td>3.000000</td>\n",
              "      <td>2.000000</td>\n",
              "      <td>2.000000</td>\n",
              "      <td>50000.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>75%</th>\n",
              "      <td>487.000000</td>\n",
              "      <td>1892.856000</td>\n",
              "      <td>8.000000</td>\n",
              "      <td>14.000000</td>\n",
              "      <td>4.000000</td>\n",
              "      <td>2.000000</td>\n",
              "      <td>2.000000</td>\n",
              "      <td>75000.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>max</th>\n",
              "      <td>648.000000</td>\n",
              "      <td>5856.468000</td>\n",
              "      <td>22.000000</td>\n",
              "      <td>38.000000</td>\n",
              "      <td>7.000000</td>\n",
              "      <td>4.000000</td>\n",
              "      <td>5.000000</td>\n",
              "      <td>250000.000000</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-0addc8c9-1af6-49b1-931b-71a65f442e50')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-0addc8c9-1af6-49b1-931b-71a65f442e50 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-0addc8c9-1af6-49b1-931b-71a65f442e50');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 6
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df.isnull().sum()"
      ],
      "metadata": {
        "id": "ZFAKbIIPlPgi",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "8815669e-e33d-447f-9edd-a53293db7eb3"
      },
      "execution_count": 21,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Unnamed: 0     0\n",
              "Sqft           0\n",
              "Floor          0\n",
              "TotalFloor     0\n",
              "Bedroom        0\n",
              "Living.Room    0\n",
              "Bathroom       0\n",
              "Price          0\n",
              "dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 21
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df.columns"
      ],
      "metadata": {
        "id": "Ltg9ghY8lPc7",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "36a7c281-0251-4dc5-cac6-034678578824"
      },
      "execution_count": 91,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Index(['Unnamed: 0', 'Sqft', 'Floor', 'TotalFloor', 'Bedroom', 'Living.Room',\n",
              "       'Bathroom', 'Price'],\n",
              "      dtype='object')"
            ]
          },
          "metadata": {},
          "execution_count": 91
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        ""
      ],
      "metadata": {
        "id": "S0E_A7vulPbV"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Matplotlib visualizations\n",
        "\n",
        "> Indented block\n",
        "\n"
      ],
      "metadata": {
        "id": "_Df6DiWIPoRe"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "plt.figure(figsize=(8,5))\n",
        "plt.title(\"Bedrooms\", fontsize=14)\n",
        "plt.bar(x=df['Bedroom'].value_counts().index,\n",
        "        height=df.Bedroom.value_counts().values)"
      ],
      "metadata": {
        "id": "se5CfvFilPZ2",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 354
        },
        "outputId": "1def6b34-3201-49ff-8363-eb7210c26d5a"
      },
      "execution_count": 23,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<BarContainer object of 7 artists>"
            ]
          },
          "metadata": {},
          "execution_count": 23
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 576x360 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "plt.hist(x=df['TotalFloor'])\n"
      ],
      "metadata": {
        "id": "xHEDNkjGlPXB",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 317
        },
        "outputId": "cffaa27c-d822-4c0e-d8db-f7ad06b31a16"
      },
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(array([ 38., 230., 167., 126.,  46.,  20.,  15.,   2.,   0.,   1.]),\n",
              " array([ 1. ,  4.7,  8.4, 12.1, 15.8, 19.5, 23.2, 26.9, 30.6, 34.3, 38. ]),\n",
              " <a list of 10 Patch objects>)"
            ]
          },
          "metadata": {},
          "execution_count": 13
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAXcAAAD4CAYAAAAXUaZHAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjIsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+WH4yJAAANaElEQVR4nO3df6jd9X3H8eerartRCyq5C0GzXVsCw40tlTvnmBQ3WeePP2KhBIWtoQjphkILGyztP7qCkA7ajsLmSNGZQqsNa50BZatkgtsftV671J91Zm3EhJjczrW1FDrU9/4436zHeH+fe/P93s+eD7ic7/mcc+55+yX3ma/fe85JqgpJUlve0fcAkqS1Z9wlqUHGXZIaZNwlqUHGXZIadG7fAwBs2rSppqen+x5DkjaUJ5988gdVNTXfbYOI+/T0NLOzs32PIUkbSpKXFrrN0zKS1CDjLkkNMu6S1CDjLkkNMu6S1CDjLkkNMu6S1CDjLkkNMu6S1KBBvEN1o5re81Avz3t07w29PK+kjcMjd0lqkHGXpAYZd0lqkHGXpAYZd0lqkHGXpAYZd0lqkHGXpAYZd0lqkHGXpAYZd0lqkHGXpAYZd0lqkHGXpAYZd0lqkHGXpAYZd0lqkHGXpAYZd0lqkHGXpAYZd0lqkHGXpAYZd0lq0JJxT7I1yaNJnkvybJKPd+sXJXkkyYvd5YXdepJ8IcmRJE8luXy9/yMkSW+1nCP314E/q6rLgCuBW5NcBuwBDlXVNuBQdx3gOmBb97UbuGvNp5YkLWrJuFfViar6drf9GvA8cDGwA9jf3W0/cGO3vQP4Uo18E7ggyZY1n1yStKAVnXNPMg28H3gc2FxVJ7qbXgE2d9sXAy+PPexYt3bm99qdZDbJ7Nzc3ArHliQtZtlxT3I+8DXgE1X14/HbqqqAWskTV9W+qpqpqpmpqamVPFSStIRlxT3JeYzC/uWq+nq3fPL06Zbu8lS3fhzYOvbwS7o1SdJZspxXywS4G3i+qj43dtNBYFe3vQt4cGz9I92rZq4EfjR2+kaSdBacu4z7/C7wx8DTSQ53a58C9gIHktwCvATs7G57GLgeOAL8FPjomk4sSVrSknGvqn8DssDN18xz/wJunXAuSdIEfIeqJDXIuEtSg4y7JDXIuEtSg4y7JDXIuEtSg4y7JDXIuEtSg4y7JDXIuEtSg4y7JDXIuEtSg4y7JDXIuEtSg4y7JDXIuEtSg4y7JDXIuEtSg4y7JDXIuEtSg4y7JDXIuEtSg4y7JDXo3L4H0MpN73mot+c+uveG3p5b0vJ55C5JDTLuktQg4y5JDTLuktQg4y5JDTLuktQg4y5JDTLuktQg4y5JDTLuktQg4y5JDTLuktSgJeOe5J4kp5I8M7Z2R5LjSQ53X9eP3fbJJEeSvJDkD9drcEnSwpZz5H4vcO0865+vqu3d18MASS4DbgJ+rXvM3yY5Z62GlSQtz5Jxr6rHgFeX+f12APdX1c+q6vvAEeCKCeaTJK3CJOfcb0vyVHfa5sJu7WLg5bH7HOvW3ibJ7iSzSWbn5uYmGEOSdKbVxv0u4H3AduAE8NmVfoOq2ldVM1U1MzU1tcoxJEnzWVXcq+pkVb1RVW8CX+Tnp16OA1vH7npJtyZJOotWFfckW8aufgg4/Uqag8BNSd6V5FJgG/CtyUaUJK3Ukv+GapL7gKuBTUmOAbcDVyfZDhRwFPgYQFU9m+QA8BzwOnBrVb2xPqNLkhayZNyr6uZ5lu9e5P53AndOMpQkaTK+Q1WSGmTcJalBxl2SGmTcJalBxl2SGmTcJalBxl2SGmTcJalBxl2SGmTcJalBxl2SGmTcJalBxl2SGmTcJalBxl2SGrTk57lL46b3PNTL8x7de0MvzyttVB65S1KDjLskNci4S1KDjLskNci4S1KDjLskNci4S1KDjLskNci4S1KDjLskNci4S1KDjLskNci4S1KDjLskNci4S1KDjLskNci4S1KDjLskNci4S1KDjLskNWjJuCe5J8mpJM+MrV2U5JEkL3aXF3brSfKFJEeSPJXk8vUcXpI0v+Ucud8LXHvG2h7gUFVtAw511wGuA7Z1X7uBu9ZmTEnSSiwZ96p6DHj1jOUdwP5uez9w49j6l2rkm8AFSbas1bCSpOVZ7Tn3zVV1ott+BdjcbV8MvDx2v2Pd2tsk2Z1kNsns3NzcKseQJM1n4l+oVlUBtYrH7auqmaqamZqamnQMSdKY1cb95OnTLd3lqW79OLB17H6XdGuSpLNotXE/COzqtncBD46tf6R71cyVwI/GTt9Iks6Sc5e6Q5L7gKuBTUmOAbcDe4EDSW4BXgJ2dnd/GLgeOAL8FPjoOswsSVrCknGvqpsXuOmaee5bwK2TDiVJmozvUJWkBhl3SWqQcZekBhl3SWqQcZekBhl3SWqQcZekBhl3SWqQcZekBhl3SWqQcZekBhl3SWqQcZekBhl3SWqQcZekBhl3SWqQcZekBhl3SWqQcZekBhl3SWqQcZekBhl3SWqQcZekBhl3SWqQcZekBhl3SWqQcZekBhl3SWqQcZekBhl3SWqQcZekBhl3SWqQcZekBhl3SWqQcZekBhl3SWrQuZM8OMlR4DXgDeD1qppJchHwVWAaOArsrKr/nmxMSdJKrMWR++9V1faqmumu7wEOVdU24FB3XZJ0Fq3HaZkdwP5uez9w4zo8hyRpEZPGvYBvJHkyye5ubXNVnei2XwE2z/fAJLuTzCaZnZubm3AMSdK4ic65A1dV1fEkvwQ8kuS74zdWVSWp+R5YVfuAfQAzMzPz3keStDoTHblX1fHu8hTwAHAFcDLJFoDu8tSkQ0qSVmbVR+5J3g28o6pe67Y/CHwaOAjsAvZ2lw+uxaD6/216z0O9PffRvTf09tzSak1yWmYz8ECS09/nK1X1T0meAA4kuQV4Cdg5+ZiSpJVYddyr6nvAb86z/l/ANZMMJUmajO9QlaQGGXdJapBxl6QGGXdJapBxl6QGTfoO1d71+fpnSRoqj9wlqUHGXZIaZNwlqUHGXZIaZNwlqUHGXZIaZNwlqUHGXZIaZNwlqUHGXZIaZNwlqUHGXZIaZNwlqUHGXZIaZNwlqUEb/vPcpfXW178ZcHTvDb08r9rgkbskNci4S1KDjLskNchz7tJAea5fk/DIXZIaZNwlqUHGXZIaZNwlqUHGXZIaZNwlqUHGXZIaZNwlqUHGXZIaZNwlqUHrFvck1yZ5IcmRJHvW63kkSW+3Lp8tk+Qc4G+APwCOAU8kOVhVz63H80laO319pg34uTZrab0+OOwK4EhVfQ8gyf3ADsC4SxqcFv9CW6+4Xwy8PHb9GPDb43dIshvY3V39SZIXFvhem4AfrPmEa8sZ185GmNMZ18bbZsxneppkYeu+Hyf8b/6VhW7o7SN/q2ofsG+p+yWZraqZszDSqjnj2tkIczrj2nDG9bVev1A9Dmwdu35JtyZJOgvWK+5PANuSXJrkncBNwMF1ei5J0hnW5bRMVb2e5Dbgn4FzgHuq6tlVfrslT90MgDOunY0wpzOuDWdcR6mqvmeQJK0x36EqSQ0y7pLUoEHHfSN8hEGSo0meTnI4yWzf8wAkuSfJqSTPjK1dlOSRJC92lxcOcMY7khzv9uXhJNf3POPWJI8meS7Js0k+3q0PZl8uMuNg9mWSX0jyrSTf6Wb8y2790iSPdz/fX+1efNGbRea8N8n3x/bl9j7nXLaqGuQXo1/E/ifwXuCdwHeAy/qea545jwKb+p7jjJk+AFwOPDO29lfAnm57D/CZAc54B/Dnfe+/sXm2AJd32+8B/gO4bEj7cpEZB7MvgQDnd9vnAY8DVwIHgJu69b8D/nSgc94LfLjv/bjSryEfuf/fRxhU1f8Apz/CQEuoqseAV89Y3gHs77b3Azee1aHOsMCMg1JVJ6rq2932a8DzjN59PZh9uciMg1EjP+muntd9FfD7wD9060P4M7nQnBvSkOM+30cYDOoPbaeAbyR5svtIhaHaXFUnuu1XgM19DrOI25I81Z226fXU0bgk08D7GR3NDXJfnjEjDGhfJjknyWHgFPAIo/8r/2FVvd7dZRA/32fOWVWn9+Wd3b78fJJ39Tjisg057hvFVVV1OXAdcGuSD/Q90FJq9P+dQzwiuQt4H7AdOAF8tt9xRpKcD3wN+ERV/Xj8tqHsy3lmHNS+rKo3qmo7o3erXwH8ap/zLOTMOZP8OvBJRvP+FnAR8Bc9jrhsQ477hvgIg6o63l2eAh5g9Ad3iE4m2QLQXZ7qeZ63qaqT3Q/Xm8AXGcC+THIeo2h+uaq+3i0Pal/ON+MQ9yVAVf0QeBT4HeCCJKffSDmon++xOa/tTn1VVf0M+HsGsi+XMuS4D/4jDJK8O8l7Tm8DHwSeWfxRvTkI7Oq2dwEP9jjLvE4Hs/Mhet6XSQLcDTxfVZ8bu2kw+3KhGYe0L5NMJbmg2/5FRv/Ow/OM4vnh7m69/5lcYM7vjv1FHka/Fxjqz/hbDPodqt3Lt/6an3+EwZ09j/QWSd7L6GgdRh/l8JUhzJjkPuBqRh9XehK4HfhHRq9O+GXgJWBnVfX2C80FZrya0WmEYvQqpI+Nnds+65JcBfwr8DTwZrf8KUbntAexLxeZ8WYGsi+T/AajX5iew+iA8kBVfbr7+bmf0amOfwf+qDs67sUic/4LMMXo1TSHgT8Z+8XrYA067pKk1RnyaRlJ0ioZd0lqkHGXpAYZd0lqkHGXpAYZd0lqkHGXpAb9L4aPVNXW1rOJAAAAAElFTkSuQmCC\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "sample = df.sample(n=200, random_state=42) \n",
        "plt.scatter(x=sample['Price'], y=sample['Sqft'])"
      ],
      "metadata": {
        "id": "9nB0EnHllPT_",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 282
        },
        "outputId": "673e5a9c-a383-4a73-e1bb-0fddf8ca61bf"
      },
      "execution_count": 28,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<matplotlib.collections.PathCollection at 0x7f36aea7fa10>"
            ]
          },
          "metadata": {},
          "execution_count": 28
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "plt.title(\"Price vs Sqft\", fontsize=15)\n",
        "plt.hist2d(x=df.Price, y=df.Sqft)"
      ],
      "metadata": {
        "id": "ulOPY_c4lPSu",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 543
        },
        "outputId": "5fb9fd1b-6abd-40e9-9b64-c4e1e2c28cab"
      },
      "execution_count": 29,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(array([[ 52.,  16.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.],\n",
              "        [ 90., 134.,  50.,   4.,   0.,   0.,   0.,   0.,   0.,   0.],\n",
              "        [  3.,  29.,  79.,  40.,   2.,   1.,   0.,   0.,   0.,   0.],\n",
              "        [  2.,   4.,  35.,  28.,  10.,   4.,   0.,   0.,   0.,   0.],\n",
              "        [  0.,   0.,   6.,   9.,   4.,   2.,   0.,   0.,   0.,   0.],\n",
              "        [  0.,   2.,   3.,   3.,   7.,   5.,   1.,   0.,   0.,   0.],\n",
              "        [  0.,   0.,   0.,   0.,   2.,   4.,   0.,   0.,   0.,   1.],\n",
              "        [  0.,   0.,   0.,   0.,   1.,   0.,   7.,   1.,   0.,   1.],\n",
              "        [  0.,   0.,   0.,   0.,   0.,   0.,   1.,   0.,   1.,   0.],\n",
              "        [  0.,   0.,   0.,   0.,   0.,   1.,   0.,   0.,   0.,   0.]]),\n",
              " array([  6100.,  30490.,  54880.,  79270., 103660., 128050., 152440.,\n",
              "        176830., 201220., 225610., 250000.]),\n",
              " array([ 359.358,  909.069, 1458.78 , 2008.491, 2558.202, 3107.913,\n",
              "        3657.624, 4207.335, 4757.046, 5306.757, 5856.468]),\n",
              " <matplotlib.collections.QuadMesh at 0x7f36aefa1bd0>)"
            ]
          },
          "metadata": {},
          "execution_count": 29
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        ""
      ],
      "metadata": {
        "id": "UNTqMYn7RDzH"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# HeatMap Visualization"
      ],
      "metadata": {
        "id": "vjX9ZD4HREGO"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "sns.heatmap(df.corr(),annot=True)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 337
        },
        "id": "4lZJAyYdPZQs",
        "outputId": "0626fdd1-9b52-49ff-d923-98f84d2b6fb1"
      },
      "execution_count": 22,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<matplotlib.axes._subplots.AxesSubplot at 0x7f36ae51d210>"
            ]
          },
          "metadata": {},
          "execution_count": 22
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 2 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAZAAAAEvCAYAAABrI5dsAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjIsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+WH4yJAAAgAElEQVR4nOydeViVRdvAf3MOICirKLu5YW6puOGKG4i7YlqZS7mnZVqmlqa5pqal9abm6/a5L2Vqmhu47wEqapm7qMBhEZRFUOCc5/vjIHAAFY4g1Du/6zoXPDP3zNzPMs8998w8M0JRFCQSiUQiKSiq4lZAIpFIJP9MpAGRSCQSiVFIAyKRSCQSo5AGRCKRSCRGIQ2IRCKRSIxCGhCJRCKRGIU0IBKJRPI/gBBilRAiWgjx5zPihRDiP0KIG0KIi0KIBi/KUxoQiUQi+d9gNdDxOfGdgGoZv+HATy/KUBoQiUQi+R9AUZRjQNxzRHoAaxU9ZwBbIYTz8/I0KUwF/+2k3b9V7J/tl3FtVdwqAGBjXqa4VeBJelpxqwBAGVPz4laBJ9qScS1KqU2LWwVikuOLWwUA0lPDxcvmUZB3jln5qh+g9xyeskxRlGUFKM4VuJftOCwjTPOsBNKASCQSyb+ADGNREIPx0kgDIpFIJCWVV+tZhgMVsh27ZYQ9EzkGIpFIJCUVnS7/v5dnJ/BexmyspkC8oijP7L4C6YFIJBJJiUVRCsUwACCE2AS0AcoJIcKAqYCpvhxlKbAH6AzcAJKBQS/KUxoQiUQiKakUjmcBgKIo774gXgE+Kkie0oBIJBJJSaUQPZCiQBoQiUQiKanotMWtwXORBkQikUhKKtr04tbguUgDIpFIJCWUwhxELwqeO41XCFEp58JbQohpQohxRavWy5FfHYUQEzMWDrsqhOhQlDpNnr2AVl364Nd/RJHkv2DBDC5fPsHZ4AA8PN7IU6Z+/TqcO3uAy5dPsGDBDIO4Dz8cxKWLRwg5f5A5s78EoGJFN+If3iAocD9BgftZtGjOc3WY/c2XBJ7358jJndStVytPmboetTl6aieB5/2Z/c2XmeFTZ07gVNBejpzcyer1i7C2sQLAzs6W7bvWEhp+jrnzp+T7ejxl3vyvCLl4iFN/7KGeR+08ZTw83uB04F5CLh5i3vyvcsWPGj2EhEe3KGtv99yyZn4ziVPn9nHw5Hbq1KuZp0zderU4dHIHp87tY+Y3kzLDbW1t2Lx9BSfP7mXz9hXY2FgDYGVtyZrNizlwYhtHTu/knX49M9O4ujmzedtyjv2xi9NBe6nwmmuu8ubMm0JwyAGOn971zHtSz6M2J878TnDIAebMy7rG02d9zpmz+zh+ehdrNy7OvCe93+7O0ZM7M3/346/yRh3D8y2KazHy48EEHN9GwPFtHD71G2Gxl7C1tQFg6Ij+HD71G0dO72T0x0PzLG/hghlcuXyCc2cDqP+MOtKgfh3OnzvAlcsnWJitjmzc8BPBQf4EB/lz49oZgoP8ATAxMWHVyu85f+4Aly4e4fMJo/LM12he7TTeAvM/+x2IEKIW0AeojX6BsSVCCHVRlefXuT1LF8wqkrw7dmyHu3tlatVqycgPP2fRj3m/6Bf9OIcRIydQq1ZL3N0r06FDWwBat25Ot26+NGzki0d9bxYsXJqZ5tatUBp7dqCxZwdGjZr4TB182reiStVKeNb35bMxU5i3YFqecvMXTGPs6Cl41velStVKePvol2Y5evgkXk270qZFd27eDGXM2A8AePLkCXO//oGpU+YV+Lr4dmhDVfdKeNRtx5hRk1j4/cw85Rb+MJPRH03Eo247qrpXor1v68w4V1dnvL29uHv3ud9T0a59K6pUqUjzBh0ZP2Yqc7+bmqfc3AVfMW7MVzRv0JEqVSrSzscLgFGfDuXE0TO0aNiJE0fPMOpT/Utw0NC+XLtyE5+Wb9Kr6/tMnTUBU1P9ciH/WTqHJf9ZRasm3fBp04v7MbEGZfn4tqZq1Yo08vDh09FT+G6hYaPhKd8unM4nH0+mkYcPVatWxKe9/p4cOXSSFp5d8GrWjZs3Qvn0M33jZ+vPO2ndojutW3RnxLBx3AkN489Lfxf5tfjpx1W093qT9l5vMnvGQk6fDOLhw3iq13Sn33tv0dn7Hbxb9qRLZx+qVq1kUFanju2o5l6ZGrVaMnLk5yx+RmNo8aI5jBgxgRq1WlLNvTIdM+pI334jadTYl0aNfdm+fQ87duwBoHfvrpQqZUb9Bj54NunIsKH9qVjRLc+8jULR5f9XDLyUARFCHBFCfCOECBRCXBNCeGWEDxRCbBNC7BNCXBdCzMuW5ichRLAQ4i8hxPRs4aFCiDlCiJCM+AZCiP1CiJtCiBHZ5MYLIYIylhvOnv7LDB1OANXzoX4PYLOiKE8URbmNfu6z58tcj+fRyKMONtZWRZJ3t26+bFi/FYDAwHPY2lrj5ORgIOPk5IC1tSWBgecA2LB+K927652uD4YPYP78xaSmpgIQk+NFlB86dvFmy6YdAJwNvoCNjTWOjuUNZBwdy2NlZcnZ4AsAbNm0g05dvQH9y0qr1Q8Yng0KwcXFCYDk5BT+OHOWJ4+fFFinzl182LRxOwBBQSF6nZxy6OSk1ykoKASATRu306Vr+8z4Od9MZsrkuehnOD7n/Du345fNvwFwLvgi1jZWODiWM5BxcCyHlZUl54IvAvDL5t/o2EV//h06t+PnjOv386YdmeGKomBpqV93rLRlaR4+iCc9PZ3Xq1fFRK3m2JHTADx6lExKyuNc5785I8/goBCsba3yvifWlgRnnP/mTTvonHH+hw+dyLwnwdnuSXZ6vdWVbb/+/kquRXb8enVmx1b9S7za61U5d/YiKSmP0Wq1HDt+hp5+nQzku3XrwLoN+jryR+A5bGxt8qwjVtZW/JFRR9Zt2Er37rkXr+3duxubt+jPT1EUypQpjVqtxsLCgtS0NBISknKlMRqdNv+/YqAwPBATRVE8gU/Qf5jyFA/gHaAO8I4Q4ukn8l8qitIIqAu0FkLUzZbmrqIoHsBx9EsP9waaAtMBhBC+6Jca9szIv6EQopUQoiF6b8ID/YcwjZ9mKIQYkd0AZeNZC4f943BxceJeWETmcVi4Jldld3FxIixck6dMtWpVaNmiCSeO7+JAwFYaNqyXKVep0msE/rGPAwFbadHi2fbV2dmRiPDIzOOIiEicXBwNZJxcHImIyJLRRETi7GwoA9C3fy8OBhx70Wm/EBcXJ8LCss45PCISF+cc18XZifBsOoWHR2Zel85dfNBoIvnz0pUXluXk7GBw/pqIqFzn5uzsSERElIGMk7P+JVbewZ7oqPsAREfdp7yDPQCrlm+gWvUqhFw5yuGTvzHli9koikIV90rExyeyct0P+B/7lemzPkelMqzOzi6OhGe75xHhkTjnuCfOLrnvW04ZgH4DenMg4Giu8J5vdmHbL4YGpKiuxVMsLMxp6+PF7p0BAFz9+zpNmjXEzs4GCwtzOnVsh5ubi0EaVxcnwu5l1ZHwMA2uOeqIq4sT4dmflzxkvFo2ISo6hhs3bgPw66+7efQombC757l9M5AFC5by4MHDXNfJaLTp+f8VAy8aRH9Wsyt7+LaMv2eBStnCDyqKEg8ghLgMVET/wn5bCDE8o2xnoBZwMSPNzoy/lwBLRVESgUQhxBMhhC3gm/E7nyFnid6gWAHbFUVJzijvaT5Pv7A0mgxdhwMs+W4WQ9977rc4/0hMTNTYlbWlpVc3GjXyYOPGn6hevTkaTTRV3T2Ji3tI/fp12PrLSjzqtyMxsRBbWDn4dNwI0tO1bP1554uFixALC3PGjf8Qv+7vF0v5Tz2eNu1a8telK/TuNohKlV9jy44VeJ/uiVqtpkmzhrRv1YvwMA0/rfqWvv3fZP3arYWuy9hxI0lPT+eXLYb3pGGjeqSkpPD339cLvczs5PT+2ndsQ9Af53j4UL/q7vVrt1j8wwo2b19BcnIKIRf+Qqstmi6dd97xY0uG9wHg2dgDrVZLhYoNsLOz4cjh7Rw8dJzbt+8WToElfBD9RQYkFsg5clgWuJ3t+GnfgjZHftn7HLSAiRCiMjAOaKwoygMhxGrAPI80uhzpdRl5C2COoij/za6QEOKTF5xHXuRr4bDsK1yWhOXcnzJixPsMGdwXgODgC1TI1uJyc3U2aOmDvmXp5uqcp0xYeCQ7duzNyCsEnU5HuXJluX8/jrg4fbfW+fOXuHXrDtWqVeHcOb29Hzy0LwPefzsz3sU1q7Xm4uJEZLYWJkBkRJSBZ+Ts4oRGkyXTp29P2ndoQ6/uA427KMCw4QN4f9A7AJw7exE3t6xzdnVxIkKT47poIg1ama6uTkRERFK5SkUqVnLj5JndmeHHT+6ibWu/zNbx07JUQsWFc4bn7+ziaHBuABpNFC7ZWvfOLo5EaqIBiImOxcGxHNFR93FwLMf9GP22DX369WTR9ysACL19l7t3wnCvVgVNRCR//XmFu3fCANj9ewCNGnswZFgp3huoP//z5y7imu2eu7g6oclxTzQRUbnuW3aZd/u9SYdObfHr+l6ua/1mry78ulXvfQwZ1o/3Br6DEKLIrsVTsndfPWXTum1sWqdvy46ZOJKwMA0jR7zPkCH9AP1z7VYhq464ujkbeJ6g91Bdsz8vOWTUajU9/Trh2TSre6xPn57s9z9Ceno6MTGxnDoVRMOG9QrPgBTT4Hh+eW4XlqIoSYBGCNEOQAhRFv2A8wkjy7MGHgHxQghH9DtgFYT9wGAhhGWGPq5CCAfgGOAnhLAQQlgB3fKR106gjxCiVIZhqwYEFlCfYmPp0jWZg9s7d+2jX//eAHh6NiA+PpHIyGgD+cjIaBISkvD01O9S2a9/b3bt0s8k2blzH21aNwegWrXKmJmacf9+HOXKlc3sFqlc+TXc3SsbVIxVKzbS1suPtl5+7P39AO+86wfoW6YJCYlERcUY6BAVFUNiYhING+m7yN551499uw8C0M7bi1FjhjKgz8hcffkFYfmydbRs1pWWzbqye1cA7/bVz1pq3NhDr1NkDp0i9To1buwBwLt9e7Jn9wEu/3WVqpU8qVOrFXVqtSI8PBKvFt0yjUf2stp7vcne3Qd5q08PABo0qktiQqKBLOi7YxITk2jQSN9r+1afHuzbcwgA/72HeTvj+r39rh/7M8LDwzS0bN0UgHLl7anqXpm7ofcIOfcn1jZW2GfMDGvVuhlXr9xg5fINmQPcu38/QJ+MPBs19iAh/hn3JCGJRhnn3+ddP/bsPgCAt48Xoz8ZRt93RuS6J0IIerzZiW1b9Qb2ablFeS1APyutaYvGmbJPsS9XFtC/9P38OrFp83Z+Wromc+B75879DOinryNNPBuQEJ+QZx1JTEikSUYdGdCvN7t27c+M9/H24urVGwbdgvfuhdO2TQsASpe2oEmTBly9eoPCQlG0+f4VB/n5DuQ9YLEQYkHG8XRFUW4aU5iiKBeEEOeBK+i7s04WML2/EKImcFoIAZAE9FcU5ZwQYgtwAYgGgp6meTr+kbMrS1GUv4QQPwOXgXTgI6UI78L4qXMJOn+Rhw8T8Pbrz4dDBtCrW+HMHN679xAdO7bj779PkJL8mKHDxmbGBQXup7GnvpyPR09i5YoFmFuYs3//Efbt01fC1au3sHzZd5w/d4DU1DSGDNU7dF4tmzJ16mekpaWj0+kY9fEXz+zfDfA/io9vawJDAkhJTmH0R1nTMg8f30FbL/0LYcJn0/lxyRzMLcw5FHCMAxljHXO/nYKZmRlbd/wfoPeqxn+qH1I7e/EgVtaWmJma0qmLD2/1HMy1qy9+BPfvP4xvhzZcuHSY5JTHfPjBhMy4E6d/p2WzrgCM/eQrflo2DwtzcwL8j+K//8iLL3oODvofw7t9K06f30dK8mM+/ShrinLA8W2093oTgImfzeT7JbMxtyjFoYDjHMo4/0ULl/Pf1Qt5d0Avwu5F8MFA/T1cOP8nflgym0MndyCE4OtpC4iL09+DGZPn8/POVQgE50P+ZO3qnw10Cth/hPa+rTl74SApKSmMGvlFZtzRk/qZVADjx05j8dJvMDc350DAUQ7468c6vvl2KqVKmbHtt9WAfiD9s0/005ybt2hMRHgkd0LvkZOiuhYAnbr6cPTQSVKSUwzKXLn2B+zK2pKWnsbo0V8SH59gEL9n70E6dmzH1b9PkpySwtChWXkGB/nTqLEvAKM+nsTKlQuxMDdn3/7D7N2XZajefrtH5uD5U5b8tJqVKxZyIeQQQgjWrNnCpWwz0l6aEt6FJV40u0SSRUnowpI7EmYhdyTMQu5ImMW/aUfCx+d25vudY96g+0uXV1Dkl+gSiURSUikhDYNnIQ2IRCKRlFRKeBeWNCASiURSUinhs7CkAZFIJJKSivRAJBKJRGIU0gORSCQSiVFIAyKRSCQSY1DkLCyJRCKRGIUcA/n3UBI+4nsU/vKr1BYGvRuMLm4VaIVtcasAwOAmYcWtAtdOli1uFQB44+Oi2bKgIKiq52c3h38IsgtLIpFIJEYhPRCJRCKRGIX0QCQSiURiFMW0UVR+kQZEIpFISirSA5FIJBKJUcgxEIlEIpEYhfRAJBKJRGIU0gORSCQSiVFID0QikUgkRiFnYb0ahBBfAn0BLaADPlAU5Y9nyJYCdgPlgDlAVUVRZhtT7oIFM+jYsR0pySkMGfopISF/5pKpX78OK1csxNzCnH37DjF27FeZcR9+OIiRI95Hq9Wyd+8hJk76mooV3bh44QjXrun3/f4j8ByjRk00Rj0DJs9ewLGTgZS1s2XH+qUvTvAS1G/dgGHThqNSqwjY7M+vS7YaxNfyrM3QqcOoVLMy346ax6k9Jw3iLSwtWHTwJ/7Yf4ZlX728rpVa16XttAEItYo/Nx8hcMkug/i6/dvh8V57FK2OtOTH+H+xkrjrES9dromHJ6UHjQKVmicHd/Nkx8ZcMqbN2mDx9kBQFLR3bvLoh1moK7lTetinCIvSKDodj7etJ+3UYaP1sGlTn4ozByNUKqI3HUCzaHuecnadm/L6ign82XE8jy7qnz+LmhWp/M0I1FYWoFP4s/MElCfGrdGkrlIHM59+oFKRHnKUtDO7DeLNvPuiqlgDAGFaClHaiuSFHyKs7SnVazQIgVCZkHY2gPTzxl2Pk1fDmfd7IDqdQs/G1Rjcpo5BvOZhElN+OUliSio6RWF0hwZ41XDj0r0YZm4/rRdSYIRPPdrVrmiUDvlGeiBFjxCiGdAVaKAoyhMhRDnA7DlJ6gMoiuKRkT4JKLAB6dixHe7ulalVqyWeng1Y9OMcWnp1yyW36Mc5jBg5gcDAc+zcuY4OHdqyf/9hWrduTrduvjRs5Etqairly9tnprl1K5TGnh0KqtJz8evcnr69ujNp5reFmm9OVCoVH8waydR+k4nVxPLtroUEBvzBvev3MmXuR8Tww2ff0/ODN/PMo9+4Afz1R25jbAxCJfCe9T5b+80lURNHv10zuBFw1sBAXNlxmovrDwFQtX0D2kzpz7b35r1cwSoVpYeMIWnmOHRxMVjNWUpa8El0YXeyRJxcMe/Zj8TJo1AeJSGs9cuzKE8e8+jH2egiwxF29lh/s4yEkCCU5CSj9Kg0exhX+kwnVRNL7T3zeLg/iJTrhkuwqMqY4zS0C0lnr2UFqlW4/ziGm6P/Q/LlUEzsLFHStEZdDoTAzPc9Hm+eh5IQh/nAaaRfP48Sm3UfUg9mGViThj6oHPUvaCXpIY/XztS3yE1LYTH0a7TXz6MkPSyQClqdjjk7z7B0iC+O1qXpt3g3rWtWoKpj1rI4yw9dxLdORd5uWoObUQ8ZtfoAe2v0xt3Rjo0fdcVErSImIZm3/7OLVjUqYKJWGXc98oOS7y3RX4gQoiPwA6AGViiKMjdH/GvAGsA2Q+YLRVH2PC/PIjzzV4ozcF9RlCcAiqLcVxQlQgjRUQhxRQhxTgjxHyHE70IIB2A90FgIESKE+AWwyPh/Q0EK7dbNlw3r9S3rwMBz2Npa4+TkYCDj5OSAtbUlgYHnANiwfivdu+sNwwfDBzB//mJSU1MBiImJfYlL8GIaedTBxrro1yqq5vE6kaEaou5GkZ6WzvFdx/D0bWogEx0WzZ0roejyaGFVrVMV23K2hBw7Xyj6OHlU5WFoFPF3Y9Clabm66wzuvg0NZFKTUjL/N7UoVSgVV+1eA11kOLpoDaSnk3byEGaNWhjIlPLpypN9O1Ae6Q2DkqB/Ieo0Yegiw/VhD2LRxT9AWNsYpYdlfXceh2p4cjcKJS2duN9OYNfBM5ec24S+aBbvQPckNTPMprUHyX/fIflyKADpD5KMbhWrXKqgexCF8jAGdFq0f/+ByesNnilvUqsp6ZfP6A902qzuHBMTEMa9uv68d58K9ta4lbXC1ERNh3qVOfL3PQMZIQSPMjyspMeplLcuDYCFmUmmsUhN1yKEUSoUDJ0u/7/nIIRQA4uBTkAt4F0hRK0cYpOBnxVFqQ/0AZa8SL1/iwHxByoIIa4JIZYIIVoLIcyB5UA3oCHgBKAoSjQwFDiuKIqHoihvASkZ//crSKEuLk7cC8tqPYWFa3BxccolExauyVOmWrUqtGzRhBPHd3EgYCsNG9bLlKtU6TUC/9jHgYCttGiRu7KXZOyd7LkfEZN5HKu5j72j/XNSZCGEYNDkofzfrJWFpo+lkx2JEXGZx4maOCwd7XLJebznw5Dj39FqUh8OTV370uWqypZHF5t1HXRxMQj78oYyzhVQu7hhNfNHrL5egolH7nutdq+BMDFFF2Vcl5qZkz2pEVmNk1RNLKbOhosvlq5ThVIu9jw8eNYg3KKKCygK1TdO4Y393+L8oZ9ROgAISzuUhKz7oCTGIaxy3wcAYW2PsC2P7s7lrDCrslgMmUXpjxaSdmZ3gb0PgOiEZJxsymQeO1qXJjr+kYHMCO967D5/C985vzBq9UG+6N4kM+7S3RjeXLiD3j/sZLJf06L1PqDQDAjgCdxQFOWWoiipwGagRw4ZBbDO+N8GeOED96/owlIUJUkI0RDwAtoCW4C5wG1FUa4DCCHWA8MLmrcQYvjTdGq1LSp1mRekyD8mJmrsytrS0qsbjRp5sHHjT1Sv3hyNJpqq7p7ExT2kfv06bP1lJR7125GYaET3xT+MTu914ezhYGIji9Yby4uQtQcIWXuAGj2a0XS0H/vG/rfoC1WrUTm7kTjtE1T25bGa/h8SPhuc2VUlbMtS5uNJPFo0t1C7MwwQgopTB3Lzkx9zx5mosfSsyV+dJ6BLeUKNLdN5dPEmCScuFY0uT4ut1QTtlSCDc1YS40hZORlhaUupXmNIvxIEyQmFXva+C7fp3tCd97xqc+FONJN/Ps7WMT1QqQR1XivPtk/9uBX9kCm/nKDF626UMlUXug6ZFGAab/Z3VQbLFEVZlvG/K5Dd1QoDmmDINMBfCPExUAbweVGZ/woDAqAoihY4AhwRQlwC3i+kfJcBywDMSrkpI0a8z5DBfQEIDr5ABTeXTFk3V2ciIiIN0kdEROLm6pynTFh4JDt27M3IKwSdTke5cmW5fz+OuDh9N8L585e4desO1apV4dy5i4VxSkVObGQs5VyyWtr2zuWIjcqfQajRoAa1PGvRaUBnLMqYY2JqyuPkFNbOXWO0PkmRD7ByyWpxWzmXJSnqwTPlr+w8g8/Xg4wu7ym6uBhU2TwOVdnyKNk8EgAlNob065dBq0UXHYlWcw+Vsyvam1fBojSWE+eSsmkl2uuXc2afb1IjYzFzyfIAzZztSdNkeQJqSwssarxGrV9nAmBa3pbXV0/k2sA5pGruk3jmMulxiQA8PHSOMnWqGGVAlKQHCOus+yCsyqIk5n0f1DWbkuqftxeoJD1EFxOGusLraK8GF0gHB+vSRGbzOKISknGwMWwUbg++zpJB7QGoV9GBJ2laHiY/pqylRaZMFQdbSpuZciPqAbXdyhVIhwKhzf94U/Z3lZG8C6xWFOW7jHHldUKINxTl2VbsX9GFJYSoLoSoli3IA4gCKgkhqmaEvfucLNKEEKb5KWvp0jU09uxAY88O7Ny1j379ewPg6dmA+PhEIiOjDeQjI6NJSEjC01Pf19uvf2927fIHYOfOfbRp3RyAatUqY2Zqxv37cZQrVxaVSn9rKld+DXf3yty+fTc/6pUIrl+4hnNlFxwqOGJiaoJXt1YEBuQ5IS4XC8Z8y9BmgxneYgj/N2sVh3899FLGAyDywi1sKzthXaE8KlM11bs15WbAOQMZ20qOmf9X8fbgQWhkzmwKjPbGVVTObqgcnMDEBNMW7UgNPmUgkxp0ApPaHgAIKxvUzhXQRWnAxATL8TNJPepP2pmjL6VHUsgNzCs7U6qCA8LUhLI9WvLAPyhLz8Rkzr0xkJAmIwhpMoKkc9e4NnAOjy7eJP5ICKVrVkRlYQZqFdbNapFyzbj9T3QRt1HZOSJsyoFKjbpmE9Kv5x7nEmWdEeal0YXfyAqzsgOTjCpqXhp1hdfRxRX8HtV2K8fd+wmExyWSlq5l/4XbtK7pZiDjbGvJHzf13c63oh+Smq7Frow54XGJpGv179KIB0mExsTjYmdZYB0KROF1YYUDFbIdu2WEZWcI8DOAoiinAXP0M1Wfyb/FA7EEfhRC2ALpwA30rtxWYLcQIhk4DjxrBHkZcFEIca4g4yB79x6iY8d2/P33CVKSHzN02NjMuKDA/ZmzqD4ePYmVKxZgbmHO/v1H2LdPP9tn9eotLF/2HefPHSA1NY0hQz8BwKtlU6ZO/Yy0tHR0Oh2jPv6CBw8K3t+bk/FT5xJ0/iIPHybg7defD4cMoFe3wp3pBaDT6lg2ZSnT1s1ApVZxcEsA967dpe/Yfty4dJ3AgEDc61Zj4vIvsbSxpLGPJ++O7cvHPh8Vui4AilbHoSlr6LVuAiq1ij+3HCX2WjjNx/Yi6tJtbgaco/5AX15rWRtdmpbH8Y8Kp/tKpyV55Q9YfjkfVCpSD+9FFxaK+TuD0N68SlrwKdJDAjGt1wjrhatBpyN53VKUpATMvNpjUrMewsoGs7YdAUhePBdt6I3nl5kXWh2hX66g+savEGoVMZsPknLtHq7j+/Dowk0eZjMmuZLGP0Lz353U3jMPFNDLuY0AACAASURBVHh46GyucZJ8o+hIDViHeZ/xIFSkXzyGcj8cU6+e6DShaG/ojYlJrSak/23Y4BD2Lph7v4uiKAghSPtjL0pMwQ2ZiVrFF92bMHLVAXSKjh6NquHuaMeSgPPUcrWnTa3XGNu5ETO2n2LDicsgYHrvFgghOB8azaqjlzBRq1AJwcQeTbErY27ctcgvhTeNNwioJoSojN5w9EH/2UN27gLewGohRE30BiSG5yCUoupXLWEIIdoA4xRF6WpsHmal3Ir9YskdCbOQOxJmIXckzKKk7Eho8eakl56nlbJibL7fORZDFzy3PCFEZ+B79FN0VymK8rUQYgYQrCjKzoxZWcvRN8gVYIKiKP7Py/Pf4oFIJBLJvw5FV3ht1oxvOvbkCPsq2/+XgRY50z2P/xkDoijKEfSD7BKJRPLPQC5lIpFIJBKjKEQPpCiQBkQikUhKKnItLIlEIpEYhTQgEolEIjGKEj5LVhoQiUQiKalID0QikUgkRlGApUyKA2lACoCNeeEtpGgsJeEDPoCt5/5T3CoQ++bg4lYBAM8jicWtAg+evPzmV4XBG4tfK24V8DRJfbHQK2Be3lvdFAw5C0sikUgkxqDILiyJRCKRGIX0QCQSiURiFAXYD6Q4kAZEIpFISirpchBdIpFIJMYgu7AkEolEYhSyC0sikUgkRiE9EIlEIpEYg5zGK5FIJBLjKOEeiKq4FTAGIYRWCBGS7VdJCNFGCPH7q9Zl9jdfEnjenyMnd1K3Xq08Zep61OboqZ0Envdn9jdfZoZPnTmBU0F7OXJyJ6vXL8LaRr8dqJ2dLdt3rSU0/Bxz508pkD71WzdgyeGlLD22jF4f9s4VX8uzNgt2f8+2W7/RvHPuzccsLC1Y+cdqhs8YUaByC8Lk2Qto1aUPfv2LrgwAM09Pyq1fS7mNGyjTL+f2z2DRsSMOO3dgv3IF9itXYNGlS2acysEBu+/mU27dGsqtXY3aySnf5Xq1a8b+079yIHAHw0cPzK2XmSnfL5/DgcAdbN23BtcKzgC0aN2E7QfW8/vRLWw/sJ6mLRvnSrt03QJ2H9uSb11mz5tMYEgAR089+/ms51GbY6d3ERgSwOx5kzPDp82cwOngfRw9tZM1GxZnPp9PcXVzJjTiPB99bNyKAJ5tGrP26P+x4cQa+n7UJ1d83SZ1WLb3Jw6G7qd1Fy+jysiL11vXY/zB75hwZCFtRnbPFe81pDOfBczn073fMGzDl9i6ljOIL2VpwaTTi+gxfWCh6fRMtNr8/4qBf6QBAVIURfHI9gstrIyFEPn2ynzat6JK1Up41vflszFTmLdgWp5y8xdMY+zoKXjW96VK1Up4+7QC4Ojhk3g17UqbFt25eTOUMWM/AODJkyfM/foHpk6ZVyDdVSoVH8wayfT3pzLK+0O8uremQrUKBjL3I2L44bPvOfbb0Tzz6DduAH/98WeByi0ofp3bs3TBrCItA5UK60/H8GD859x/733Mvduhrlgxl1jKocPEDhlK7JChpOzenRlu++UkHm3azP0B7xP7wUi0Dx7ks1gV0+Z+wdA+o+nUojdde3bA/fXKBjK9+/mR8DABH08//m/pBsZ/pV+e5kHcQz7o9wldW7/DhFFTmb9khkE63y5tSX6Uku9L4OPbWv98erRn7JgpzF84PU+5+Qun8+noyXh6tNc/n+31z+eRwydp2aQLrZt35+aN23yS8Xw+ZebsiRwMOJZvfbKjUqkYM+tjPh8wiffbDqFdj7ZUrGa4DEp0eDRzx87jwI5DRpWRF0Il6DljECsHfsN37cfh0b05Du6uBjIRl0P5T7cvWdjpcy7t/YMuEw0bHx0+e4vbgVcKTafnolPy/ysG/qkG5LkIIcoKIXYIIS4KIc4IIeq+IHyaEGKdEOIksC6/5XTs4s2WTTsAOBt8ARsbaxwdyxvIODqWx8rKkrPBFwDYsmkHnbp6A3Dk0Em0GS2Hs0EhuLjoW7nJySn8ceYsTx4/KdB5V/N4nchQDVF3o0hPS+f4rmN4+jY1kIkOi+bOlVB0efStVq1TFdtytoQcO1+gcgtKI4862FhbvVjwJTCtWQNteDhajQbS03l88BDmLfO33bO6YkVQq0kNPguAkpICT/J3L+o2qM2d0HvcuxNOWlo6u3f4492pjYGMT6fWbNuid5b37TpIMy9PAC5fukp01H0Arl+5ibl5KczMTAEoXcaCQSP7s2TBinzpAdCpszc/b9oOwNmgC9jYWD37+QzSP58/b9pO5y4+gOHzGRx0ARfXLC+sUxcf7t4J4+qVG/nWJzs1PKoTHhqB5q6G9LR0Dv12hBa+hvcnMiyKW3/fLtRxgAoe7ty/E0ncvWi0aVou7DpNbd9GBjI3T18m7bF+Pa27529g41Q2M871jcpYlrPh2vGLhabT81B0Sr5/xcE/1YBYZOu+2p5H/HTgvKIodYFJwNoXhAPUAnwURXk3v0o4OzsSER6ZeRwREYmTi6OBjJOLIxERWTKaiEicnQ1lAPr272V0a+4p9k723I+IyTyO1dzH3tE+X2mFEAyaPJT/m7XypXQoKajKlUcbnXUttDExqMqXzyVn3roV9v+3EtsZ01E56ONNKlRAl5SE7awZ2K9YjtXIEaDKX1VxcnZAEx6VeRwZEYWjc46XtlN5IjNktFotSQlJ2JW1NZDp2M2bvy5eITU1DYBPvhjJqiXrSUl5nC89AJxdHAkPy/Z8hkfhnOP5dHbJ8QznIQPQb0DW81mmTGlGfzqM+XMX5VuXnJR3LkeMJjrzOCYyhvLO+XtWXwYbRzviI2Izj+M1sVg72j1TvvHbbbhyRG9chRB0ndyf3V9vKHI9M5EeSJGQvQurZx7xLcnwJBRFOQTYCyGsnxMOsFNRlFz9A0KI4UKIYCFE8OPUh0VyMp+OG0F6upatP+8skvzzQ6f3unD2cDCxkbEvFv6X8PjUKWLe7kPsoCE8CQ7GZtJEfYRajVndOiQu/onYD0agdnHGolPHV6aXe/UqjJ8ymq/GzQag5huv81olNwL2HH5lOmTn6fP5yxb98zlh4scsXbyaR4+Si0WfV0V9v5a41a3C0WW7AGg2oD1XDocQHxn36pTQ6fL/KwbkLKwsHuUVqCjKMmAZQHmb6srgoX0Z8P7bAJw/f8nArXdxcSIyIsogfWREVGbXFICzixMaTZZMn749ad+hDb26D3zpE4iNjKWcS1Zr1965HLFR+TMINRrUoJZnLToN6IxFGXNMTE15nJzC2rlrXlqv4kB3Pwa1Q9a1UJcvjy4mxkBGSUjI/D/l991YjdD38etiYki/cUPf/QU8Pn4C09q1YDcvJFITjbNrVgveycWRKI1huVGRMTi5OhKpiUatVmNpbcmDOH3jxMnZgSVrvmX8qK+4GxoGQP1GdXnDoxaHz+7CxERN2XJlWb/jv/T3MxyTABg8rF/m8xly7hKubtmeT1dHNDmeT01ElOEznEOmT9+e+HZsy5vd3s8Ma9CoHt16dGDqjPHY2FijU3Q8fpLKymXrX3yBMojR3Ke8s0PmcXmn8sRoir7xEh/1ABuXLE/HxtmehKjc41vuLd6g3Sg/lr4zA21qOgAVG1SjUuMaNBvQnlKlzVGbqklNfszebzYXncIlfBbWv9WAHAf6ATOFEG2A+4qiJAghnhWe74xXrdjIqhUbAWjv25ohw/uz/dfdNGxUj4SERKKicrwsomJITEyiYaN6nA2+wDvv+rHiv/phlnbeXowaM5QenfsXqGviWVy/cA3nyi44VHAkLjIWr26t+G70/HylXTDm28z/2/X2xr1utX+s8QBIu3IVtZsbamcntDH3MfduR/wMw4F7lX1ZdLH61mSpFs1Jv3M3I+0VhKUlwsYGJT4eswYNSL96NV/lXjp/mUqVK+D2mgtRmmi6+PkydsSXBjIH9x3lzXe6EhJ8iY7dvDlzIggAK2tLlm38gW9n/si5wAuZ8htXb2Xj6q0AuFZwZtmG7/M0HgCrlm9g1XJ9F0v7Dm0YMrw/27bupmHjeiQkJD37+Wxcj7NBF3j73Z5Zz6ePFx9/MozunfoZPJ/dOmYNKk+Y+DGPkh4VyHgAXL1wFbfKrjhVcOJ+5H3a9WjDrFGzC5SHMYRduEm5Sk7YuZUnISqOet2asWm0YVecS+1K9Jo9lJXvz+VRbFYjY9MnizP/b9i7FW51qhSt8QAUrfwOpDiYBqwSQlwEkoH3XxBuFAH+R/HxbU1gSAApySmM/mhSZtzh4zto6+UHwITPpvPjkjmYW5hzKOAYBzL6kud+OwUzMzO27vg/AIKDLzD+06kAnL14ECtrS8xMTenUxYe3eg7m2tWbz9VHp9WxbMpSpq2bgUqt4uCWAO5du0vfsf24cek6gQGBuNetxsTlX2JpY0ljH0/eHduXj30+epnLUGDGT51L0PmLPHyYgLdffz4cMoBe3ToUbiFaLQnf/4Ddt/NBpSJlz17SQ0OxHDyItKtXeXLyFKV79aJUi+ag1aJLSCR+zlx9Wp2OxCU/Ufb7BSAE6VevkbwrfzPEtVot0yfOY9XPi1Cr1Gzd9Bs3rt5izOcjuBRymUP7j/HLht/4dslMDgTu4OGDeD4drn9uBgx9h4qVKzBq3DBGjRsGwMC3PiLufv5mgOUkYP8RfHxbE3ThgP75/HBiZtzhE7/RtmUPACaMncaPP83F3MKcgwHHOOCvn6E399uvKGVmxtbfVgP6iR7jMp7Pl0Wr1fHDlB+Zv2EuKpWKvVv2EXrtDoPGvc/VC9c4FXCa6vWqM2vFNCxtLGnWvhkDx77PIO+hL1WuTqvjt69WM3TtRFRqFUE/HyHqehi+n/Ym7NJtLh84S5eJfTErbU7/JWMAeBgey+ph374g5yKihHsgQinhm7aXJMrbVC/2i9XcplpxqwDIHQmz4/V3SdiRsPh1AHjDuiTsSJh7skRxMC90U/67Np5BwpD2+X7nWK8MeOnyCsq/1QORSCSSfzzFNT03v0gDIpFIJCUVaUAkEolEYgxKujQgEolEIjEG6YFIJBKJxChK9izef+yX6BKJRPKvpzDXwhJCdBRCXBVC3BBCfPEMmbeFEJeFEH8JITa+KE/pgUgkEklJpZA8ECGEGlgMtAfCgCAhxE5FUS5nk6kGTARaKIryQAjhkHduWUgDIpFIJCWUQpzG6wncUBTlFoAQYjPQA7icTWYYsFhRlAcAiqJE58olB9KAFIAn6WnFrQKtsH2x0CugJHzEZ79tVXGrAIBNnZda0KBQELzyb8jyxE5lUdwqUDVdXdwqFBpKev5lhRDDgeHZgpZlrOUH4ArcyxYXBjTJkcXrGfmcBNTANEVR9j2vTGlAJBKJpKRSgC6s7Au/GokJUA1oA7gBx4QQdRRFeeYy5HIQXSKRSEooii7/vxcQDmTfntQtIyw7Yei3tUhTFOU2cA29QXkm0oBIJBJJSUVXgN/zCQKqCSEqCyHMgD5Azg2IdqD3PhBClEPfpXXreZnKLiyJRCIpoeTDs8hfPoqSLoQYBexHP76xSlGUv4QQM4BgRVF2ZsT5CiEuA1pgvKIoz92kRRoQiUQiKaEUlgEBUBRlD7AnR9hX2f5XgLEZv3whDYhEIpGUUBRtyZhd9yykAZFIJJISSmF6IEWBNCASiURSQlF00gORSCQSiRH8z3kgQgh74GDGoRP60fyYjGNPRVFSs8l+gv5ryeQX5HkEGKcoSrAQIhRIzMgX4EMgAvhdUZQ3Cus8jGXe/K/w7dCG5JTHjPxgPBdC/sol4+HxBj8tm4+FeSn89x9hwvgZBvGjRg9h9pwvqfRaQ+JijdsPG6BS67q0nTYAoVbx5+YjBC7ZZRBft387PN5rj6LVkZb8GP8vVhJ3PcLo8rJj5umJ9ehRoFKTsns3jzYYrstm0bEjVh+OQBtzH4DkbdtJ2b0bAJWDAzafj0ft4ACKwoMJX6CNjCwUvZ4yefYCjp0MpKydLTvWLy3UvJu19WTcjDGo1Cp2bPydNYs2GMSbmpky/T9fUrNudeIfJDDxg6lowvTn516zKpPmjaOMVRkUnY73Og3HxETN8h2LM9M7upRnz6/+LPjqx+fq4dWuGV9+PQ61WsUv63ew7D9rcukxf/F0aterycO4eD4ZNpHwexqat27CuCmjMDU1JS0tjXnTfuDMiWAAOvu1Z8Qng1GrVRz2P8G3M5+vQ3bqt27AkGnDUKlVHNgcwLYlWw3ia3nWZvDUYVSqWYnvRs3j9J5TmXFbb+/g7pU7AMRExDBnyKx8l5uTCm3q0ny6vl5c2XSEkMWG9aJm/3bUHphRLx495tjnK3l4PYLyHlVo9c0QAISA4AXbCd0XbLQe+UFR/sc8kIxpXx4AQohpQJKiKM/akf4TYD3wXAOSB20VRbn/9EAIUanAiuaBEMJEUQqyeIAhvh3aUNW9Eh5129G4sQcLv59JuzZv5pJb+MNMRn80kaCgEH7dvor2vq0J8D8KgKurM97eXty9m/Mbn4IhVALvWe+ztd9cEjVx9Ns1gxsBZw0MxJUdp7m4/hAAVds3oM2U/mx7b95LlQuASoX1p2N4MHYc2pgY7Jct5fGJk2jv3DEQSzl0mMTvf8iV3PbLSSStW0dq8FmEhQWKrvCbYX6d29O3V3cmzXzWo2kcKpWKz2eP5aN3PiVKE8Pavcs55n+S29dCM2V6vNuFxPhEejZ/F98e3nw8eQSTRkxDrVYzc9EUvvp4Jtcv38TGzpr0tHRSn6TSr33W0jHr9q/g8J5jL9Rj6tzPGfTWR0RGRPGr/1oO7jvGzWu3M2Xe6teD+IeJtPfsSRc/X8Z/9TGfDJvEg7iHjOj3KdFR96lWoyqrfv4Rr7qdsbWzYcLUMfT06c+D2Id8s2gazbwac/p4UL6uy/BZI5jWbwqxmljm7VpAYMAfhF3PWl0jJiKGHz/7nh4f9MyVPvVxKmM7jXlhOS9CqAQtZr3P7r5zeaSJ483dMwj1P8vDbPXixo7T/J1RLyq2b0Dzqf3Z038eD66Esa3zFBStjtIOtvT2/5o7AedQtEXnJujSS7YBeSUfEgohvIUQ54UQl4QQq4QQpYQQowEX4LAQ4nCG3E9CiOCMpYSnG1mWuRDi/zLKOi+EaPuC8IFCiJ1CiENkeU5G0bmLD5s2bgcgKCgEGxtrHJ3KG8g4OpXHysqSoKAQADZt3E6Xru0z4+d8M5kpk+ein1FnPE4eVXkYGkX83Rh0aVqu7jqDu29DA5nUpJTM/00tSsFLlpmZV80aaMPD0Wo0kJ7O44OHMG/ZIl9p1RUrglpNavBZAJSUFHjypFD0yk4jjzrYWFsVer6169fkXmg44Xc1pKel4//bQVp3aGkg07qjF7//rF9i6ODvR/D00t+Xpq0bc/3vm1y/fBOA+AcJ6HIYz9eqVMDO3pbzZy48V4+6DWpzJ/Qe9+6Ek5aWzu4d/vh0am0g492pNdu3/A7Avl0HaeblCcDfl64SHaVvn12/cpNS5qUwNTOlQkVX7ty6y4NY/coWp44G4tu1Xb6uSzWPamhCNUTdjSI9LZ0Tu47h6Wu4FFNMWDR3roQW6T7gDh5VSQiNIjGjXtz47QyVctSLtGz1wqR0qcy6mP44NdNYqEuZFlZ1eS6Kkv9fcfAqxkDMgdWAt6Io14QQa4GRiqJ8L4QYi6E38aWiKHEZSw8fFELUVRTlYh55HhZCaIEniqLkXBDsI/RTmusIIWoA/kKI158TDtAAqKsoStzLnKiLixNhYZrM4/CISFycnYiKjMmScXYiPCKrOyY8PBIXFydAb4A0mkj+vHTlZdQAwNLJjsSIrNNJ1MTh7FE1l5zHez40HNYJtakJP/eZ/dLlAqjKlUcbnXXO2pgYTGvVyiVn3roVZvXqor0XRsKiReiiYzCpUAFdUhK2s2agdnIm9exZEv+7DIrACykKHJzKExWetYhptCaGN+rXzCFTjqgIvYxWqyUp4RE2ZW14rWoFUBR+3PQddva2+O84yNolhl1/vj28Cdh56IV6ODo7EBkelXkcGRFNvYaGPbyOTg5oMmS0Wi2JCUnYlbXhQVx8pkyHbt5cvniFtNQ07ty+R2X3irhWcCYyIhqfzm0wNc3fK6Sskz33IzI7DYjVxPK6x+vPSWGIWSkz5v++AG26lm1LfiXQ/0y+02antLMdSZqsevEoMg6H+rnrRe33fagzrBNqMxN2vZNVLxzqV6X1t8OwcivHoTFLi9T7ADmIDvqvHm8rinIt43gN+pf593nIvp2xoqQJ4AzUAvIyIAZdWDloCfwIoCjKFSHEHfSf5D8rHCDgWcYj+wqXpczsMTOxft65Go2FhTnjxn+IX/dXu7JryNoDhKw9QI0ezWg62o99Y//7Ssp9fOoUKQcPQloaFt27YTNpIg8+GQtqNWZ16xA7ZBja6Ghsp32FRaeOpOze8+JM/+Go1WrqedbhvU7DeZzymJ9+/p6/L14l6MTZTBlfP2+++njmK9HHvXoVxk/5mEFvfwRAQnwiU8fP5fvlc9DpdJwPushrldxeiS7Dmw0mLioOx9ccmbHpa+5eDSXyTuGOi2XnrzUH+GvNAdz9mtFgtB9HPtXXi+jzN/nF+wts3V1o+/0H3Dt8Ae2Tolulu6QbkBKzFpYQojIwDr2nUhfYjd57eRU8elaEoijLFEVppChKo7yMx7DhAzhx+ndOnP6dyMho3NycM+NcXZyI0Bg+5BGaSFwzPA4AV1cnIiIiqVylIhUruXHyzG4uXT6Gq6sTx0/uwsGxnFEnlBT5ACuXspnHVs5lSYp69oD8lZ25u7iMRXc/BrVDVtedunx5dDExBjJKQgKk6Steyu+7MX1db8t1MTGk37ih7/7Sanl8/AQmrz93PbcSRXRkDI6uWfvwODiXJzryfg6Z+zi66GXUajWW1mWIj4snWhPD+TMXiI+L50nKE04eOkONOlmt9Gq1qqJWq7ly8RovIkoTjZOrY+axk4sDURrD7R2iIqNxzpBRq9VYWVtmeh+Ozg4sXjOfCaOmci80azzusP9x3uo4kHc6D+b2jTvcvnk3X9clLjKWci5Zz7K9sz2xUc9dJcMwfZS+fRd1N4o/z/xJ5dpV8p02O8maB1g6Z9WLMk5leaR5dr248dsZKnXIXS8e3ogg7dFj7KoXrQEt6V1Yr8KAaIFKQgj3jOMBwNGM/xOBpx3R1uhf5PFCCEegk5HlHQf6AWR0Ub0GXH1O+EuxfNk6WjbrSstmXdm9K4B3++oHABs39iAhIdGg+wogKjKGxMQkGjf2AODdvj3Zs/sAl/+6StVKntSp1Yo6tVoRHh6JV4tumX3RBSXywi1sKzthXaE8KlM11bs15WbAOQMZ20pZL5gq3h48CC2cFl3alauo3dxQOzuBiQnm3u14cvKUgYzKPqsSl2rRnPQ7dzPSXkFYWiJsbAAwa9AAbajh4HtJ5nLIFSpUdsOlgjMmpib49vDm2P4TBjLH9p+g69sdAfDu2oagE/r7cvrIH7jXrEopi1Ko1WoaNPXgVrbB9w5+PuzfcSBfelw6f5lKlSvg9poLpqYmdPHz5eA+w4H3Q/uO0fOdrgB07ObN6RP6wXAra0uWb/ye72Yu4lyg4VhL2XJ2AFjbWNF3cG9+Wb8jX/pcv3Ad58ouOFRwxMTUhJbdWhEUEJivtGVsymBipu8ssbKzpkajmty7fu8FqfIm+sItbCo7YZVRL9x7NOVOjnphXTmrXlT09iDhtr5eWFUoj1DrX5mWrvbYVnUh6Z5h/S5sFJ3I9684eBVdWI+BQcAvQggT9KtCPp03uQzYJ4SIUBSlrRDiPHAF/cYnJ40sbwnwkxDiEpAODFQU5YkQ4lnhxp9ZDvbvP4xvhzZcuHSY5JTHfPjBhMy4E6d/p2UzfWUd+8lX/LRsHhbm5gT4H8V//5FC0+EpilbHoSlr6LVuAiq1ij+3HCX2WjjNx/Yi6tJtbgaco/5AX15rWRtdmpbH8Y8Kr/tKqyXh+x+w+3Y+qFSk7NlLemgoloMHkXb1Kk9OnqJ0r16UatEctFp0CYnEz5mrT6vTkbjkJ8p+vwCEIP3qNZJ3/V44emVj/NS5BJ2/yMOHCXj79efDIQPo1a3DS+er1WqZP2khP276DrVaxc7Nu7l1LZQPxg/h7wtXOOZ/kt827WbGj5PZfmoTCQ8TmDRiGgCJ8Uls+O8W1u5dDorCyYNnOHnwdGbePt3bMab/+HzrMWPifFb+/CNqlZqtm3Zy4+otRn/+AX+G/M2h/cf4ZcNvzF8yg4DA7cQ/SODT4ZMA6D/0HV6rXIGPxg3lo3FDARj01iji7j9g8tfjqFFb7xEu/nYFobfy54HotDqWT1nK1HXTUalVHNxygHvX7vLu2H7cuHSdoIBA3OtW4/Plk7C0saSxT2P6jO3HGJ+PcHOvwMg5H6HTKahUgm1LthrM3ioIilbHiSlr6LxhAkKl4uqWozy4Fk6jcb2IuXCbOwHneGOgL64ta6NL1/Ik/hGHM7qvnDxfx+PDbujStSg6hRNfrubxgySj9MgvuhK+lIl42dk+/0tYl6lS7Bdrqn3z4lYBgH6VwopbhRKzI2GzErAjYUJ6youFXgG1LZxfLFTEdNTZFLcKAHwQtv6l3/7XanbM9zvn9b/3vXJrI79El0gkkhLK/9yHhBKJRCIpHEr6LCxpQCQSiaSEUtJHGKQBkUgkkhKK9EAkEolEYhRaXYn5VC9PpAGRSCSSEorswpJIJBKJUejkLCyJRCKRGIOcxvsvoozpq1qa69kMblL8H/ABeB5JLG4VsCkBH/ABnL605sVCRUyY9wfFrQIA9o0eF7cK3PAv2eMGBUF2YUkkEonEKOQgukQikUiMQo6B/D975x0fVdE14Gd2N5UU0rt06RCQIkjvRZpIB0WRIoJ0BaQJUgTsgAjqC68iTRFQauhdelFqgFDSey9b5vtjl02WBFIIEL/3Pvzuj70zZ2bOPdmdM+3OKCgoKCgUiRI+gqU4EAUFBYWSitIDIOosKQAAIABJREFUUVBQUFAoEsoqLAUFBQWFIvF0T1x/chQHoqCgoFBC0Ss9EAUFBQWFomBAcSAKCgoKCkVAlnAHUrLfUlFQUFD4H8ZQiCs/hBAdhBDXhBDBQojJj5HrKYSQQoh6+eX51HsgQgg9cAkQgB4YJaU8Voj0s4AUKeXip6Nh4Znz6VRat21Geno6Y0dO5dKFK7lkatWuxpfL5mFrZ8veoENM/3AeAKVLO7P8P58R8IIf9+6GMnzweBITk3B0cmDJik/x8/dBo9bw7ZL/sH7N7wD4+fvw2dez8fXzxqmUmpR5kzFER+SpmyawAfZvjQKVmsy928jc/EsuGatGLbDrPRikRH/nJqlffYK6bEXsh45D2NkjDQYyNv2M9tj+AtukaatGTJs7EbVazYafN7Pi61UW8dbWVixcOpsatauSEJfImKGTCb0XzivNGzJx+misrKzQarV8OusrThw5ZZF2+U+fE1DGj87N+uSrR6OWDZg4ewwqtYrNv/zJ6iVrLJ/d2oqPv/6IqrUqkxifxJThMwm/b7RlxaoVmLpwIqUcSyENBt7oOAyNRs3KzUvN6b18Pdj+224+n/FNgW3zOKbN+5xDR0/i6lKazT8vL5Y888KucT1cPxyJUKlI/n0HiT+ut4h36NoO13FD0UXFApC0bgspv+9A4+OJ5xezQKgQVmqS1m4heeOfRdZDXaMetv1GIoSKrMM7yNqxPpeMpl4zbLq9AVJiuHeL9JXzsyNt7XGY8z26c8fI+GVJkXRwalEH/1lDQa0idm0Qkct+y1OudMdGlF8xmaudJ5B2MRiX7s3xGtHdHG9XtSxXO44n/fLtIulREIqrByKEUANLgbbAfeCUEGKrlPLyQ3KOwBjgr4Lk+yyGsNKllIEAQoj2wHyg+ZNmKoTQSCl1T5pPYWnVthnly5ehcd0O1K1XiwWfzaRzm7655BZ8PoOJY2Zw9vRF1mz8jlZtmrJvz2FGjXuHIwdPsOTL7xk19h1GjXuHubM+5613+nP96k3e7Psebm4uHD69nU0b/kSr1fL18vl8tfg7Dh04zuUuZcDwiPaGSoX9kDGkzJmIIS4ax/nL0Z4+iuH+nWwRbz9sewwgedooZGoKwqk0ADIzg9Rv5mGICEW4uOH06QqSzp9CpqXkaxOVSsWsBZMZ3GskEWGR/Lb7J/btPEjw9ewf1usDupOUkESbBt3p3L0dk2a8z9ihU4iPS2D4gLFERcZQqUoFftywhKa1OprTtevckrTU9AL9bVQqFR/OG897fcYRGR7Nf3es5NDuo9y+HmKW6davM8mJyfRo3I923VozetoIpo6YhVqtZs6S6cwYPYcbl2/i7OKETqsjKzOLAW3fNqf/adf37N9+qED6FITundrSv2dXps55iu0jlQq3qaOJGP4husgYfH9ZQtqB42hv3bUQS919kNj5lpWyLjqOsEFjQKtF2Nni99tK0g4cRx8dW3g9hAq7AaNJ/exDZHwMpaYvQXf+OIbwbD1Unn7YdO5H6vyxkJaCcCxtkYVNj8Hor18qfNnmAlQEfDKcG/1nog2PpfKfi0kMOknGjXuWYqXs8BjShdSz18xh8ZsPEr/5IAC2VcpQ4fspT9V5ABRjBdcACJZS3gIQQqwDugGXH5KbA3wKTCpIps96CMsJiH9wI4SYJIQ4JYS4KIT4OEf4R0KI60KII0DlHOEHhBBfCiFOA2OEEK2FEOeEEJeEED8KIWxMco8KDxFCzBdCnBdCnBZC1BVC7BJC3BRCjCjIA3To1IqN67YAcPb0RZycHfH0creQ8fRyx9HRgbOnLwKwcd0WOnRuDUD7Tq3YsHYzABvWbjaHSylxcCgFgL2DPQnxieh0Ol6sXAGNWs2hA8eNmWekQ1ZmnrqpK1bBEBGKISocdDq0R/dhXe8VCxmbNq+SuXMzMtXoGGRSAgCG8PsYIkKNYfGxGBLjEU7OBTEJtepW507IPe7dCUWr1bFt825ad2xhIdOmY3M2rTe2XHf+sZdGTRsAcPnSNaIiYwC4cfUmtrY2WFtbGe1Qyo633h3Iss+/L5Ae1etU5V5IKKF3w9Fpdezespfm7ZtYyDTv0JQ/N+wEYO+fB2jQ9CUAXm5enxtXbnLj8k0AEuOTMDzkqF8oH4CLW2nOnbhQIH0KQr3Amjg7ORZbfnlhU6My2nth6EIjQKcjdecB7Fs0LlhinQ60WgCEtRVCVfQqQ12+MoaoMGRMBOh1aE8eQFPHUg+rZh3J2rcVTA0XmZxgjlOVqYTKqTS6y2eKrEOpwEpkhkSQdTcSqdURv/Uwzu0a5JLzndifyGW/YcjMyjMf125Nid96pMh6FBSJKPAlhBhmqtceXMNyZOUH5PSS901hZoQQdYEAKeW2gur3LByInanCvgp8j9HDIYRoB1TC6BkDgZeEEM2EEC8BfU1hnYD6D+VnLaWsh7E7tgroI6WsibE39a4Qwjav8Bzp75p6RIdNcq8DLwMfUwC8fTwJC80ePgoPi8THx8tCxsfHi7CwSAsZbx9PADw83cwVZlRkDB6ebgD8uHINlSqX5/zVg+w/uoXpk+chpaR8xbIkJibzw09fsfvQb9gNGgGP+BGrXD0wxEab7w1x0Qg3D0sZnwDUvv44zvkGx7nL0ATm/vGoK1ZBaKwwRIYVxCR4+3gSHpr9vBFhkXj5WJbr5e1BhElGr9eTkpSCi6tl67JDl9b8c/EqWVnGCmvs5Hf5cdnPpKcXbIdXT28PIkOjzPdR4dF4ej/k3L3diQyLyqFHKs6uzrxQIQCk5Ju1n/Hz7h94Y2T/XPm369aaoK37CqRLSULt6Y4+Ivt7oY+KQfNQowfAvnUT/DZ+h+fi6ai9sv9+ai8P/DZ+R8CuX0j4z/qi9T4AUdodQ1y2HjI+BlVpSz1U3v6ovPywn/wl9lO/Rl3DNAwvBLa9h5OxYUWRyn6AlbcbWWEx5ntteCxW3m4WMnY1ymPl607Svkc7KpcuTYjbUnw90UdhEAW/pJQrpJT1clwFNpYQQgV8DkwojH7PwoGkSykDpZRVgA7Af4UQAmhnus4BZ4EqGB1KU+B3KWWalDIJ2PpQfg8GTSsDt6WU1033q4Fmjwl/wIP8LgF/SSmTpZTRQKYQwrJGAwuvnpYV/3D0EyNN+zW3aNWEfy5dJbBKc9o0fY15i6bh4FgKtVpNw0Yv8fG0RXRs2RuVpw/WLToUvUC1GpWPP8mzxpL61WxKDZ+IsHcwR4vSrpQaPZXUZZ8+072kK1Yuz6Tp7zNjonGuqGqNF3mhrD9B2ws+D/MkqNVqajeoybT3ZjOk20hadGxK/SYvWci0696aXZv3PBN9njVpB49zr+MgQnsNJ/3EWTw+yR7B0EdGE9prOPe7DMaxa1tUrrl+JsWHSo3Ky4+0RRNIXzEPuzfHgV0prFp2RXfpJDI+Jv88ngQh8J/xNqFz/vNIEfvAFzGkZ5Jx7e4jZYoLA6LAVz6EAgE57v1NYQ9wBGoAB4QQIRgb1Vvzm0h/pkNYUsrjgDvggXFSfb7JuQRKKStKKX8oQDapT6jGg/EfQ47PD+5zzQmZvPp/pJSao3/tJyoyGl8/b3O8j68X4eGRFmnCwyPx9fWykIkIN7Z6o6NizUNenl7uxETHAdB3QA+2/2GsnEJu3+XunftUrFSe8LAI/vn7Knfv3Eev16M9dQR1uUp5PpghLhpVjh6HytUDmaNHAiBjo9GeOgp6PYaoCPTh91D5mHqydvY4TFlA+tof0N94eGj00USER+Hjl/283r5eRIZblhsZEY23SUatVuPg5EB8nHF4wtvHk2WrFzNp1AzuhhjPO6lTrxY1Aqux/8wfrPvzB8pWKMPPm797rB5REdF4+Xma7z19PIiKiHlIJgYvX88cepQiMS6RqPBozp24QGJcIpnpmRzdd4IqNV80p6tUrQJqtZqrF6/zb0MfFYPaO0ePwtMdXaSlXQyJyeahquRNO7Cp+iIPo4+OJSs4BNu6NYukh0yIQeWarYdwcceQYKmHjI9Bd/4E6PXImAgMkaGovPzQVKiKdatuOHz6Eza9hmHVuA02PYcUWgdtRCzWvtm9HisfN7QR2T0qlYMddpXLUGnDJ1Q/toJSdSpT/sePsK9V0Szj0q0pcVsOF7rsoiALceXDKaCSEKKcEMIa4yiPuXEupUyUUrpLKctKKcsCJ4CuUsrTj8v0mToQIUQVQA3EAruAt4UQDqY4PyGEJ3AI6C6EsDOtCOjyiOyuAWWFEA/+soOAg48JfxKWAoFtm77Gjm176dW3GwB169UiOSnZPCT1gKjIGJKTU6hbrxYAvfp2Y+d249DH7h376d3PuJKjd7/u7DKFh94Pp0nzlwFw93CjQsVy3A25x/mzf+Pk7IibmwsAmhp1LSbFc6IPvobKxx+VpzdoNFi90oqs05YL3rJOHUFTPRAA4eiM2icAQ2Q4aDQ4TJpD1sHdaE8UzlyXzl2mbLkA/F/wxcpKQ+fu7di70zKPvTsP8lqfVwHjUNWDlVaOTg6s+OUrFs/5hrMns+cWfln1K01qdqDlS13o++oQQm7eYWD3xx+adPn8VQLK+eMb4IPGSkO7bq05tMtynPrQriO82tvYg2v9agtOHTkLwPEDf1GxagVs7GxQq9XUfTmQWzkm39t3b/Ov7X1k/nMNqxf80PgZvxelOrQg7eBxCxm1u6v5s32LRmTdNrau1Z7uCBtrAFSODtjWqYE2xHLCuaDob19D5eWHcPcGtQarBi3QnbfUQ3vuKOrKxt+NcHBC5eWHjA4nfeUCUj4YQMqHg8jcuALtsT1k/laQ9qYlqRduYFPWB+sAT4SVBpeuTUkMOmmONySncbH2IP5pPIx/Gg8j9dw1br09l7SLwUYBIXB59RXitz4bB1Jcy3hNC45GYax3rwAbpJT/CCFmCyG6FlW/Z7EKy04Icd70WQBvSin1wG4hRFXguHFEixRgoJTyrBBiPXABiMLoOXMhpcwQQrwFbBRCaExyy6WUmXmFF9fD7N19iNZtm3H83E7S0zIY995H5rigw5to2/Q1AKZMmGNaxmvDvqDD7Asyjpcu+WIl3636gn6DenL/XhjDB48H4ItF3/LVsnnsO7oZIQRzZ31OnKmFPnvaIjZs/RGBgOhbZO59xDJKg560H77C4aNFoFKRtX8Hhvsh2PZ5C/3Na2hPH0N3/iRWtevh9MUqMBhI+2k5MiUJ66Zt0VStjXB0xrqlsYJNW7oAfUhwvjbR6/V8PGUhP25Yglql5te1Wwi+dosxH47g0vnL7Nt1iI1rtrB42Rz2nNxMQnwi44ZNBWDQO30oUy6AUROHMmriUAAG93qPuJjCDxfq9XoWTf2Cb9Z+hlqtYuu6bdy6HsLwSUO4cuEqh3YfZcvabcz+Zhq/H1tLUkISU0fMAiA5MYU1363nvztWgpQc3XuCo3uzK7c2XVsxZmCBFqYUikkzF3Dq3EUSEpJo3X0gI4cMomeX9sVbiN5A7PwleH87H1QqkjfvQnvzDqVHvknWP9dJO3gcp/7dsW/RCKnTY0hKJmb6IgCsyr+A24ThSCkRQpC4eiPa4JCi6WEwkLFmCfbj5iNUKrKO7MIQdgebbm+iD7mO7sJx9H+fRlP9JUrN+d4ov3ElMrUYT7/UG7g3fQUVf56FUKuIXb+XjOv38JnQn7SLwRbOJC8cGlZHGxZD1t3Ix8oVm7qi+F4klFJuB7Y/FDbjEbItCpKnkCX9zMQShE/pas/dWJfbeuYv9AwoEUfaauyftwqAcqRtTtzyffXs6RO8u2R8L+re2/LEtf96nwEFrnP6hK955q+tK1uZKCgoKJRQDCV7JxPFgSgoKCiUVJTNFBUUFBQUisRzHzPPB8WBKCgoKJRQlCEsBQUFBYUioX/eCuSD4kAUFBQUSihKD0RBQUFBoUgoZ6IrKCgoKBQJxYH8PyJTr33eKnD9qGv+Qs+A+MyC7dT7NBElZIljSXiJz3/v4/cJe1ZEdn7neavASZ7u9vgFpW4x5CFLxlf8kSgOREFBQaGE8sxPzCskigNRUFBQKKEo74EoKCgoKBQJZRWWgoKCgkKRUCbRFRQUFBSKhOJAFBQUFBSKhDIHoqCgoKBQJHTKHIiCgoKCQlFQeiAKCgoKCkXCUMJdiCo/ASFESh5hI4QQb+ST7nshRLUnUS5HXiFCiEtCiItCiINCiDLFkW9xMH/hdE6f38Ph439Qq3bej1s7sDpHTvzJ6fN7mL9wujn8408+5MSZnRw+/gf//WUpTs7GN2hf792Vg0e3mq+YxGvUqFm1QPo4t6hDrcPfUPvoUnxG9XiknEunl2kYtolStSqYw+yqlqHa1vnU3P8lNfd+gbCxKlCZOZm3cBonzwdx8NjWx9rj0PE/OHk+iHkLp5nDZ835gOOnd3Lw2FZWr8m2xwP8/H0ICTvHe6PffmT5TVs1Yufx3wg6+TvD3n8zV7yVtRVfrpxH0Mnf2bhzFX4BPgA0bt6QTXt+4o+D69i05ydebpJ9Nmun7m3ZemAt2w6vZ+L00YWyB4Bd43r4bfkR/z9W4fx2n1zxDl3b8cL+jfiuX47v+uU49OgIgMbHE991y/Bdvxy/TStx7PVqocsuCNPmfU6zzn3pPnDEU8n/ATYv18drw2q8f/0Jxzf65Yq379wen52b8PxpBZ4/rcC+aydznN+xIHO426JPnkiPgBa16HtgEf0Of0bgyC654qsNbEWvoPm8vnMu3X6bjkslXwA8A8vz+s65xmvXXMp2ePrn9xoKcT0P8nUgeSGlXC6l/G8+Mu9IKS8XTa08aSmlrAUcAKblI/tMaNOuORUqlKFeYBvGvT+dz76Ynafc4i8+ZuzoadQLbEOFCmVo07YZAAf2HeWVBp1p2qgLN4NDGDfB+AP+dcNWmr/SleavdGXE0IncCbnP35eu5K+QSkXZeUO5NuATLrYYg1u3pthV8s8tVsoW73c6k3LmenagWkXFb8YQMvk7LrUcy5XXpyO1hdtMuk275pSvUJYGgW0ZP2Y6i774OE+5RV98zLj3p9EgsC3lK5Sl9QN77D9Kk4adad64KzeDbzN2vOUWIXPmTWFv0KHHPL6KmQs+ZGjf9+n0Si9e7dGeCi+Ws5DpNaAbiQnJtG3Qg1XLf2HSDKNDiI9LYMSAcXRp3pcPR81i0TLj37K0izMfzBzDmz3fpXPTPnh4udGoaf2CG0Wlwm3qaCJHTuV+j3co1aElVuVfyCWWuvsgYX1GENZnBCm/7wBAFx1H2KAxxvABo3F+qw9qD7eCl11Aundqy/LPn6xSzheVCpdJY4gZO5mIvm9h164VmnK524Hpew4QNWgYUYOGkbZ1uzlcZmaZw2MnFf3nL1SCJp+8ybY3FrK+1QdU7Pay2UE84Mbm42xsO4VfO3zE+eXbaDRjIABxV+/zW+fp/NrhI7YPWkTz+W8h1EWqQguMLMT1PCjS0wshZgkhJgohqgghTuYILyuEuGT6fEAIUc/0OUUIMVcIcUEIcUII4WUKr2C6vySE+CSv3k4eHAf8cpS3z9Qz2SuEeCGf8FVCiG9NZd4SQrQQQvwohLgihFhVWDt06tyGdWs3A3D61HmcSjvi5eVhIePl5YGjkwOnT50HYN3azXR6tS0A+/cdQa/Xm9P7+nrnKqNnr1fZ9NufBdLHoU5FMkLCybwbidTqiNtyBJf2DXLJ+X/Qn/ClmzFkZpnDnJsHknblDmmXQwDQxaeAoXDtmo6dWrNh7e8AnDl1AWfnR9jD0YEzpy4AsGHt73Tq3AYwOtRse1zA1y/bHh07t+Hunftcuxr8yPJr1a3OnZB73LsTilarY9vm3bTp2NxCpnXH5vy+3mjPnX/spVFTo32uXLpGVGQMADeu3sTG1gYraysCyvhx59Zd4mMTADh28CTtXm1VYJvY1KiM9l4YutAI0OlI3XkA+xaNC5ZYpwOtcf81YW2FUD2dyqpeYE2cnZ7u/lHW1aqgux+KPiwcdDrSg/Zh16yAdihGPAMrkBQSSfLdaAxaPTe3nqBsu5csZLQp6ebPVvY2II3Vsy4jC6k3/ibUNlYPgp8q/y97IA+QUl4FrIUQD5p5fYD1eYiWAk5IKWsDh4ChpvCvgK+klDWB+wUstgOw2fT5G2C1qWeyBvg6n3AAF6ARMA7YCnwBVAdqCiECC6gDAD6+XoSGhpvvw0Ij8PH1yiUTFhqRLROWWwZgwKDX2RN0MFd4j9c6s2ljwRyItbcbWWGx5vus8FisfCw3X7SvWR4bXzcS9p6xCLcr7wtSUvmX6dTYtRifkd0LVGZOfHy9CL2f41lDI/O3Rx4yAAMG9TT3NkqVsuf9cUNZtGDJY8v38vEkIjTSfB8RFoWXj6eljLcn4SYZvV5PclIKLq7OFjLtu7Tm8sWraLO03Ll9j3IVy+AX4INaraZNpxb4+OXW91GoPd3RR0Sb7/VRMWi83HPJ2bdugt/G7/BcPB11Dqer9vLAb+N3BOz6hYT/rEcfHZsr7b8Btac7+sgo870+Kga1h0cuObuWTfH8eSWu82ei9syOF9bWeK76Fo8flmDb7JUi61HK24WUsDjzfUp4HKW8XXLJVX+zDf2OfMbLU/tydEb2YItnYAV671lA76D5HJr6H7NDeVrohCzw9TwojibNBoyOAx7tQLKAB7XgGaCs6XMjYKPp8y/5lLNfCBEKdATW5kj/IN1PQJN8wgH+kFJK4BIQKaW8JKU0AP/k0MuMEGKYEOK0EOJ0pjYxHxWLxviJ76LT6di4fqtF+Ev1apOens6VKzeKpyAhKDNzMHc+XpU7TqPGoUFVbo76ksvdp+LSoSFOTWoWT7mFZNzEEeh0erM9PpgymuVLV5GamvbUy65YuTyTpo9m+sR5ACQlJjNz0gK+XDmfX/5YSejdMAzFXGmkHTzOvY6DCO01nPQTZ/H4ZJI5Th8ZTWiv4dzvMhjHrm1RuZYu1rJLEhmHjxPevT9RA4eSefIMLjMnm+PCu/cjavC7xE2fS+lx76H2831MTk/OP6v3sLbJBE7MX0fd97MbU1Hnb7KhzWR+e3UGdd/rgroI84SFoaQPYRXHKqz1wEYhxCZASinzqu20pkobjKc0FqXclkACxh7Fx8D4oigLZJr+N+T4/OA+l15SyhXACgBXx0pyyNABvDHY6C/Pnb2In5+PWdbXz5vwsEiL9OFhkRZDMb6+ljL9BrxG+44t6f5q7jUJr/XszG+/Fqz3AZAVEYu1b/YYubWPG9rw7NaW2sEOuyovUO23OQBYeZTmxVVTuD54PlnhMSSfuIwuLhmAhH1nKVWzPElHLj22zLeHDmDQm70BOH/2En7+OZ7Vzyt/ezwk07d/D9p1aMlrXbInwOvWq02Xbu2ZOXsSzs5OGKSBjMwsfl9t6XAjw6PwztE78Pb1JDI8ylImIgofPy8iw6NQq9U4OjkQH2dsGHj5eLJ09SI+GDWTeyGh5jT7dx9m/+7DAPQZ1AN9IRyIPioGtXeOHoWnOzrTUNkDDInJ5s/Jm3bgOnYoD6OPjiUrOATbujVJ23O4wOWXFPRRMai9snuDak939NHRFjKGpCTz59Qt23EeNSw7LtpoM31YOJlnz2NduSLpoYU/UiA1Ih4H3+xeuYOPK6kR8Y+UD95ygqZz38oVnhAchjY1A9fK/kRfvF1oPQpKSX8T/Yl7IFLKmxidwnTy7n08jhNAT9PnvgUoSweMBd4QQrgCx3KkGwA8+GU9KvyJ+WHlGvME97Y/99C3n7F1Uq9+IEmJyURGWv4oIiOjSU5KoV594+hY337d2b5tDwCt2zTl/bFD6d9nBOnpGRbphBB0e60jm37dVmDdUs4HY1vOB5sAT4SVBtduTYjffcocr09O42yNwZxvOILzDUeQcvY61wfPJ/XiTRIPnMe+ahlUdtagVuHUqBrp1/MfVfxx5RpaNulGyybd2L5tD737GVd+vVS/NklJKXnbIzmFl+rXBqB3vx7s2L4XgFZtmjJ67FAGPmSPLh36U7dmK+rWbMV3367my8XL+WHFz7l0uXTuMmXLBeD/gi9WVho6d2/H3p2Wk+77dh6iRx/jaqYOXVpz/IjRPo5ODqz85Us+m7OEsycvWKRxdTcOcTg5O9L/7dfZ+PNmCkrmP9ewesEPjZ83aDSU6tCCtIPHLWTU7tkVmn2LRmTdvmsM93RH2FgDoHJ0wLZODbQh9wpcdkki68pVNAF+qH2MdrBr24r0Q5Z2ULll28G2aWO0IUY7CEcHsDK29FXOTljXroH29p0i6RF14RbOZb1xDPBAZaWmQteXCQk6ayHjXDa7EVKmdSCJIcYhV8cAD/OkuYOfG6Ur+pJ8z/L7XdwYkAW+ngcF6QnYCyFy1iSf5yGzHlgElMsj7nGMBX4WQnwE7ATMY0RCiPNSylxzElLKcCHEWuA9YDTwHyHEJCAaeNBUeFR4sRK06wBt2zXnzIW9pKenM+rd7C73waPGlVQAk8bPYunyT7G1tWVP0EH27DbOdXy6eCY2NtZs2rIKME6kTxg7A4DGr9QnLDSCO4WpMPQGQj76nsq/zECoVUSv20v69Xv4TepL6oWbJORwJrmSJqYS/t1Wqm9fCBIS9p3JNU9SEHu0adecUxf2kJ6Wzvsjp5jj9h/ZQssm3QD4YPwsvvl2AbZ2tuwNOmS2x4LFM7CxtuZXkz3OnDrPxHEzC/74ej2zpyzihw3foFap+XXtVoKv3eL9D4fz9/kr7Nt1iI1rtrBo2WyCTv5OYnwS44ZNBWDgO314oVwA7018h/cmGg9FeqvXKOJi4pk2dyJVqlcCYOni7wm5dbfgRtEbiJ2/BO9v54NKRfLmXWhv3qH0yDfJ+uc6aQeP49S/O/YtGiF1egxJycRMXwSAVfkXcJswHCklQggSV29EGxxS8LILyKSZCzh17iIJCUm07j6QkUMG0bNL++ItRG8gYfE3uH/9KUKlJvWPHehuh+A0bDBZV66TcfgYDn1ew65pY6RejyEpifjZnwKpWbu6AAAgAElEQVRgVbYMLpPHme2QvHotuiI6EKk3cGT6ajr//AFCreLa+oPEXw+l3oSeRF+8zZ2gs9QY3A6/JtUx6PRkJqayf5zxsC7v+i9SZ2QXDDo90iA5/NEqMuILsu6n6JTst0BAyGexlOBRhQthD6RLKaUQoi/QT0rZ7bkplA+ujpWe+99zh+PzmZd4mM4pfz9vFXC1cXreKgCwyzf3JOyzRjmRMJs/w57u/EhBGXHv5yfeiGR82b4FrnM+D1n3zDc+ed5vor8ELBFCCIzzG49+Q0xBQUHhf4zn3mLNh+fqQKSUh4Haz1MHBQUFhZJKSZ9Ef949EAUFBQWFRyBLeB9EcSAKCgoKJZSS3gN5uhu5KCgoKCgUmeJcxiuE6CCEuCaECBZCTM4jfrwQ4nKOLaDy3bRWcSAKCgoKJRQ9ssDX4xBCqIGlGHfyqAb0y2O39HNAPdMWUL8CC/PTT3EgCgoKCiWUYtxMsQEQLKW8JaXMAtYBFq9MSCn3Sykf7Bd0Asi9lfdDKA5EQUFBoYQiC/Ev5759pmtYjqz8gJxvJd83hT2KIcCO/PRTJtELgY366W6cVhBqjH66224XlBpLc59p8axxUdk9bxUAcKuXkb/QU6YkvMAH4LXt++etAr2HPpWNJ54LhZlEz7lv35MghBgI1AOa5yerOBAFBQWFEkoxLuMNBQJy3PubwiwQQrQBPgKaSykzH45/GGUIS0FBQaGEUoxzIKeASkKIckIIa4ybzVpsZy2EqAN8B3SVUkblkUculB6IgoKCQglFX0x7FUopdUKIUcAuQA38KKX8RwgxGzgtpdyKcUNcB4zHcwDclVJ2fVy+igNRUFBQKKEU5zbtUsrtwPaHwmbk+NymsHkqDkRBQUGhhKJsZaKgoKCgUCRK+lYmigNRUFBQKKE8r5MGC4riQBQUFBRKKPltUfK8URyIgoKCQgnleZ4YWxCeigMRQuiBS4AA9MAoKeWxx8iXBvpLKZeZ7lsAE6WUrz4N/Z6UOZ9OpXXbZqSnpzN25FQuXbiSS6ZW7Wp8uWye+dzv6R/OA6B0aWeW/+czAl7w497dUIYPHk9iYhLvjn6b13obH1ejVlOpcnlqVGhCQkIi74wYyIA3eiGEQBP6F7pTux+pm7p8TazbDACVCt35g2hPbLOIt27dH1WZKgAIKxuEvSNpX4xEOLlh0/N9EAKh0qA9E4Tu3P5isVeDFvUZ9fFI1GoV29bu4Jel6yxt1bAmo2aNpELV8sx+7xMObjtcLOXWaV6XIbOGolKr2LMuiE3LfrWIr9agOm/PHErZqmX5bNRCjm/P/or+enszd68az92ODotm/pBPiqyHukY9bPuNRAgVWYd3kLVjfS4ZTb1m2HR7A6TEcO8W6SvnZ0fa2uMw53t0546R8cuSIulg83J9So8fhVCpSN26neT/rrWIt+/cHufRw9FHxwCQsnEzaVuNC3b8jgWhvXkbAH1EFLGTphVJh/yYNu9zDh09iatLaTb/vPyplAFgVacB9kNGg0pF5p5tZGz6JZeMdeOW2PUdjJQSfchNUr+YA4DD9IVoKldDd+USKXOnPDUdH/C/OoSVLqUMBBBCtAfm8/jX4ksDI4FlhSlECKGWUuqLrGURaNW2GeXLl6Fx3Q7UrVeLBZ/NpHObvrnkFnw+g4ljZnD29EXWbPyOVm2asm/PYUaNe4cjB0+w5MvvGTX2HUaNe4e5sz7n229+5NtvfgSgbYcWDBv5BgkJiVSuWpEBb/SiU+s+ZGVpuXN6Hfrg88j4PN7zEQLrdm+QsW4hMikO28Gz0N04h4wNM4tk7c3+sWheaoPKy7hjs0xJIOO/c0CvAysb7N6Zi/7GOWRKwhPZS6VSMeaT0Uzs/yHR4dEs37aUo7uPcefGXbNMVGgUC8YvpM/w3k9U1sPlDvtkBLMGTCc2PJaFf3zOyaC/uH8jezug6LBovpnwJd2G98iVPisji/Edxzy5IkKF3YDRpH72ITI+hlLTl6A7fxxDePbzqzz9sOncj9T5YyEtBeFY2iILmx6D0V+/VHQdVCpcJo0hevQk9FHReK76lvTDx9DdvmMhlr7nAAmLv86VXGZmETVoWK7w4qZ7p7b079mVqXMWP71CVCrsh40ledYEDLHROC38jqyTRzHcz7aFyscP254DSJryHjI1BeGc/ffI2LwOYWOLTfsuT0/HHJT0SfRn8Sa6ExAPIIRwMO0zf1YIcUkI8WA3yAVABSHEeSHEIlOYgxDiVyHEVSHEGtO56QghQoQQnwohzgK9hBD9THn9LYT49EGhjwlPEUIsEkL8I4TYI4RoIIQ4IIS4JYR47EszAB06tWLjui0AnD19ESdnRzy93C1kPL3ccXR04OzpiwBsXLeFDp1bA9C+Uys2rN0MwIa1m83hOenesxObfzW2/iq9WIGzZy6Snp6BXq9Hf+8qmhfr5ambyrc8hvhIZEI0GPTor/yF5sW6j3wWTbWX0V0+Ybwx6I3OA0CjAVE8X40qgZUJDQkj/G44Oq2OfVsO8Eq7VyxkIu5HcuvKbaSh+H4ulQIrER4STuTdSHRaHUf+OESDdg0tZKLvR3HnagjS8PRaeerylTFEhSFjIkCvQ3vyAJo6jS1krJp1JGvfVkhLAUAmZzttVZlKqJxKo7t8psg6WFergu5+KPqwcNDpSA/ah12zxvknfMbUC6yJs9PT3etNU6kqhvBQDJFGW2Qd2Yd1gyYWMjZtu5C543dkqunvkZj999BdOotMT+NZUZjNFJ8HT8uB2JmcwVXge2COKTwD6CGlrAu0BD4zOYbJwE0pZaCUcpJJtg4wFuPe9eWBnLVOrCmPQ8CnQCsgEKgvhOguhPDNK9yUthSwT0pZHUgGPgHaAj2A2fk9mLePJ2GhEeb78LBIfHy8LGR8fLwIC4u0kPH28QTAw9ONqEjjMEFUZAwenm6WhrOzpWWbpmzbGgTAtSs3aNjoJVxcnLGzs0VdoTbCyTVP3YSDCzIpznwvk+MQji55yzq5IUp7YLhzOTvM0RW7IZ9g/94XaE9se+LeB4CHjzvR4dm9peiIaDx83B6Tonhw9XYjJizGfB8bHoubV8HLtbaxZtGfn7Ng8yIatHu5yHqI0u4Y4qLN9zI+BlVpywaHytsflZcf9pO/xH7q16hrmBoIQmDbezgZG55sfzy1pzv6yOy/gT4qBrWHRy45u5ZN8fx5Ja7zZ6L2zI4X1tZ4rvoWjx+WYNvslVzp/k0IV3f0Mdm2MMRGo3Kz/Huoff1R+QbgOG8JTguWYVWnwbNW00xxHij1NHgWQ1iNgP8KIWpgnBOZJ4RohrF35gd4PSKPk1LK+6Y8zgNlgSOmuAeDyPWBA1LKaJPcGqAZIB8RvhnIAnaa0l8CMqWUWiHEJVMZFpi2RB4G4GTnXWhD5MfDk2RtO7Tg1F9nSUhIBODG9Vss/ep71v3+PWlp6Rgi74J88pa6plpD9FdPQY7yZXIc6T9MQziUxqbnGHRXT0Fa0hOX9W9kWKO3iYuMw+sFL2avncvdayFE3InIP2FRUKlRefmRtmgCwsWDUh9+RsqMYVg1aoPu0klkfEz+eTwhGYePk7Z7H2i1lOrxKi4zJxPz3gQAwrv3wxAdg9rXB4+lnxF98zb60LB8cvwXo1aj9vEnefoYVG4eOM79hqQxbyFNPcRnSXFtZfK0eOpDWFLK44A74AEMMP3/ksnBRAK2j0iacydIPZbOLvUJVNLK7Frb8KAcKaWBPByqlHKFlPI/UkrN0b/2ExUZja9ftiPx8fUiPDzSIk14eCS+vl4WMhGmVnh0VKx5yMvTy52Y6DiLtDmHrx6w9qdNtG/Rix6d3kBmpGKIy7sikynxFr0T4eiKTI7PU1ZdNcfwVa58EjBE30cd8GKe8YUhOjwGD1PvC8DD24Po8Ngnzjc/4iJicffNblm6+bgRG1nwcuMijX+XyLuR/H3ib8pVL18kPWRCDCrXHK15F3cMCZYOQcbHoDt/AvR6ZEwEhshQVF5+aCpUxbpVNxw+/QmbXsOwatwGm55DCq2DPioGtVf230Dt6Y4+OtpCxpCUBFotAKlbtmNdpVJ2nGliXR8WTubZ81hXrlhoHUoKMi4GtXu2LVRuHhhiLf8ehthosk4dBb0eQ1QEhrB7qHzzPVvpqfC/OoRlRghRBePmXbGAMxBlavG3BB6cuZsMFGXw8yTQXAjhbjqysR9w8DHhRWUpENi26Wvs2LaXXn2NUzd169UiOSnZPCT1gKjIGJKTU6hbrxYAvfp2Y+f2fQDs3rGf3v2Mo2m9+3VnlykcwNHJgZdfqW+WfYCbu9Ep+Pn7oKn8Erp/8q74DWG3Ubl4IZzdQaVGXbUhuhvncskJVx+ErT2G0ODsMEcX0JjOO7G1Rx3w4iMdVWG4duEa/uX88A7wRmOloVW3FhwLeuSCvGLjxoUb+JTzxTPAC42VhiZdmnEq6GSB0pZyLoXG2tiWcHRxokq9qty7cS+fVHmjv30NlZcfwt0b1BqsGrRAd/64hYz23FHUlY3fFeHghMrLDxkdTvrKBaR8MICUDweRuXEF2mN7yPzth0LrkHXlKpoAP9Q+3qDRYNe2FemHLHVQuWU3PGybNkYbYpzkF44OYGX8XqicnbCuXQPtQ5Pv/yZ0N66i8vFH5Wm0hXWTVmhPHbWQ0f51BKsagQAIR2dUvgEYIp9Pj+t/dQjLzjTsBMZhqzellHrTUNIfpuGi08BVACllrBDiqBDib4ynYG3LM9eHkFKGmw6H328qZ5uUcgvAo8KflL27D9G6bTOOn9tJeloG4977yBwXdHgTbZu+BsCUCXNMy3ht2Bd0mH1BhwBY8sVKvlv1Bf0G9eT+vTCGDx5vTt/x1TYc3HeU9LR0izJ/+O9XuLiWRqvTkrnrJ8h8xCSeNJAV9BO2fSeBUKG7eAgZE4pV0x4YwkPQBxudiaZaQ3RX/rJIKtx8sW3dDyklQgi0f+1ARt9/UnOh1xv4avo3LFqzAJVKxY71Owm5foe3Jr7JtQvXORZ0nMq1K/PJ97NwcHagUdtGDB7/Jm+1frIDkgx6AyunL2fmTx+jUqvYu34P967fpd/4AQRfusGpoJNUrFWJD1dOxcHZgfpt6tN3/ADGtHkP/4oBvDv/PQwGiUol2LTsV4vVW4VTxEDGmiXYj5uPUKnIOrILQ9gdbLq9iT7kOroLx9H/fRpN9ZcoNed7o/zGlcjU5Cd6fgv0BhIWf4P7158iVGpS/9iB7nYITsMGk3XlOhmHj+HQ5zXsmjZG6vUYkpKIn21cd2JVtgwuk8eZvxfJq9fmWr1VXEyauYBT5y6SkJBE6+4DGTlkED27tC/eQgx60lZ+iePMxcZlvHu3o78Xgl2/t9EFX0V76hjacyexCqyP89erkQYD6au/RSYbh3Id536D2u8FhK0dpVduJHXpQrTnTxWvjjko6e+BiJKuYEnCp3S1526s4A/rP28VAOi8NNdZNM+cknIi4eq2z/9EwqS/n+lq9kdSEk4kTC4hJxK6/n5QPGkeLf3bFrjO2X8/6InLKyzKm+gKCgoKJRR9MSyYeZooDkRBQUGhhPLchzzyQXEgCgoKCiWU/9WtTBQUFBQUnhDFgSgoKCgoFImSvshJcSAKCgoKJRSlB6KgoKCgUCQMyiosBQUFBYWioPRA/h8RnZb4vFVAVbny81YBgAaarOetAhV06uetAgDBu5/FqQiP52SRdgIqfnqXgJf4HFf+53mrUGwocyAKCgoKCkVC6YEoKCgoKBSJ57XLbkFRHIiCgoJCCcWgDGEpKCgoKBQFZS8sBQUFBYUioQxhKSgoKCgUCWUIS0FBQUGhSCg9EAUFBQWFIlHSeyDP/w0oBQUFBYU8MUh9ga/8EEJ0EEJcE0IEm478fjjeRgix3hT/lxCibH55/it7IEIIPXAJo/5XMJ65nuugcCHEMSll46etzxefz6Zjh1akpaczZMg4zp3/O5dM3To1+eGHL7CztWXHzn2MGz8DgF/WfMuLL1YAoLSzEwmJSdSr3w6NRsOK7xZTp04NNBoNP//8K58uXJKvLkevhbLwz5MYDJIe9SvxdouaFvHhCSlM33iU5PQsDFLyfvu6NK3iz6V70cz5/bhRSMKINrVpVb1MkW3yYvPadJvxBkKt4uT6/Rz4dqtFfNMhnWjQtyUGnYGUuCQ2fvAdCaEx5ngbBzsmBC3in92n2TJzVZF0CGhRi8YfD0KoVVxde4DzS/+wiK86sBXVB7dF6g1oUzM49OEPJNwIwyOwPM0+HQKAEHD6898J2Xm6SDoAOLWog/+soaBWEbs2iMhlv+UpV7pjI8qvmMzVzhNIuxiMS/fmeI3obo63q1qWqx3Hk375dqF1CGhRi1dmGW1xZe0Bzi+ztEW1ga2o/mYOW0z+gfgbYXgGlqfZAqMtEHD6i6LbwqpOA+yHjDaeRb5nGxmbfsklY924JXZ9ByOlRB9yk9Qv5gDgMH0hmsrV0F25RMrcKUUqvyBMm/c5h46exNWlNJt/Xv7UyikoxfUioRBCDSwF2gL3gVNCiK1Syss5xIYA8VLKikKIvsCnQJ/H5fuvdCBAupQyEEAIsQYYAXz+IFIIoZFS6p6F8+jYoRWVKpajSrUmNGxQl6VL5tO4SZdcckuXzGfEiA/46+RZ/tz6Ex3at2Tnrv30H/CuWWbRpzNITEoC4PXXX8XGxpo6ddtgZ2fLpQsHWLd+82N10RsMzN96guVD2uHlZM+ApdtoXjWACl6lzTIr912kXc0y9H65CjcjExi1ag87qrxORS8XfnnvVTRqFdFJafT++g+aVQlAoy58J1WoBD1mv8XKgfNIjIhl9Na5XA46Q1Rw9jnqYZdD+LrLR2gzsnh5YBs6T+nPmlFfm+PbT+jF7ZNXC112Th1e+eRNtvVfQGp4HK9tm03I7jMk3AgzywRvPs6Vn/cBUKZtXRrPHMj2gQuJv3qfTZ2mI/UG7D1L8/ruudwJOovUF2FJpUpFwCfDudF/JtrwWCr/uZjEoJNk3LhnKVbKDo8hXUg9e80cFr/5IPGbDwJgW6UMFb6fUiTnIVSCJp+8yZ8PbPHnbO4EnSE+hy1ubD7O5Ry2aDRjINsHLSTu6n1+65xti167imgLlQr7YWNJnjUBQ2w0Tgu/I+vkUQz372SL+Phh23MASVPeQ6amIJyzv7cZm9chbGyxaZ/7t1WcdO/Ulv49uzJ1zuKnWk5BKcatTBoAwVLKWwBCiHVANyCnA+kGzDJ9/hVYIoQQ8jFK/H8YwjoMVBRCtBBCHBZCbMVkFCFEygMhIcSHQohLQogLQogFprAKQoidQogzprRVClt4ly7t+WnNrwD8dfIszqWd8fb2tJDx9vbE0cmRv06eBeCnNb/StWuHXHm9/noX1q3fAhi/OKVK2aNWq7GzsyNLqyUpKSVXmpz8fS+GADcn/F0dsdKoaV+7HAeuWFZUQghSM7UApGRk4eFkD4CdtcbsLLJ0eoQorCWyCQisSMydCOLuRaHX6rnwx3Gqt6tnIXPz+GW0Gcb9tO6eC8bZ29Uc51ejHA7uzlw/fLHIOngGViApJJLku9EYtHqCt5ygbLuXLGS0Kenmzxp7G/OPVZeRZa4g1TZWPMlvuFRgJTJDIsi6G4nU6ojfehjndg1yyflO7E/kst8wZOa9x5hrt6bEbz1SJB0etsXNrY+3hZW9DRSzLTSVqmIID8UQGQ46HVlH9mHdoImFjE3bLmTu+B2Zavyey8QEc5zu0llkeq5BhmKnXmBNnJ1Kxr5iYOyBFPQSQgwTQpzOcQ3LkZUfkLMyuG8KIy8ZKaUOSATcHqffv7UHAhh7GkBHYKcpqC5QQ0p5+yG5jhi9a0MpZZoQ4kFttQIYIaW8IYRoCCwDWhVGBz9fb+7fy27Jhd4Px8/Xm4iIKAuZ0PvhuWRy0rRJQyKjogkONqr+22/b6NqlPffvnsPe3o4JE2cRH5/A44hKSsPbuZT53svJnkv3oi1kRrSuzbs/BrH22FXSs3R89047c9ylu9HM/O0o4QmpzO3dpEi9DwBnLxcSw2LN94nhsQQEVnykfP3eLbh64AJgdHCvThvIurFLqdikRpHKB7D3cSElPM58nxoRh2edCrnkqr/ZhppDO6K21vBHn3nmcM86FWi+eCiO/u7sG7O8aL0PwMrbjayw7KE5bXgs9nVetJCxq1EeK193kvadwWtEjzzzcenShJtD5uUZlx+lvF1ICcu2RUp4HF6PsEWtoR1RWz1ki8AKtDDZYu/YotlCuLqjj8n+TRhio9G8WNVCRu3rD4DjvCUIlYr09avQnjtZ6LL+P1GYHoiUcgXGOu2Z8W/tgdgJIc4Dp4G7wA+m8JMPOw8TbYD/PJgnkVLGCSEcgMbARlNe3wE+DyfM6dUNhtSn8SwA9OnTnfWm3gdAg/qB6PV6AsrUpeKLLzNu3HDKlXvhicvZeeE2XV+qyO4pvVgyuDXTNhzGYDB+SWu+4MGmcd1Z815nfjhwiUxt/hNzT0qd7k3wr1WegyuMY/KNBrXl6v7zJEbE5ZOyePhn9R7WNZnAX/PWUff97PmGqHM32dh6Mps6z6DOqC6obayejgJC4D/jbULnPHoHWfvAFzGkZ5Jx7e7T0cHEP6v3sLbJBE7Mf8gW52+yoc1kfnt1BnXfe4q2UKtR+/iTPH0MKZ/Pxn7kJIS9w9Mp61+CQcoCX/kQCgTkuPc3heUpY2qcOwOxPIZ/aw/EPAfyAGEccylMDa8CEh7O52FyenWNtZ8EeHfEmwwZMgCA06fP4x/ga5b38/chNCzCIo/QsAj8/H0eKaNWq+nRvSMNXu5oDuvbtwe7dh9Ap9MRHR3LsWOneOml2o99IE8neyISs00QmZSGZ44eCcDvp2+w7K22ANQu40mmVk9CWgauDnZmmfKepbG3tiI4Mp7q/u6PLTMvEiPjcfbN7vk6+7iRFBmfS67iKzVoNao7y/vMRp+lA6BM3UqUrV+FRoPaYmNvi9pKTVZaBjs+XVcoHdLC43HwyR4WK+XtSmp4bh0eELzlBE3m5d6KPCE4DG1qBi6V/Ym5WPj5B21ELNa+2Ta08nFDG5H9m1Q52GFXuQyVNnxijPdwofyPH3Hr7bmkXQwGwKVbU+K2HC502Q9IjYjHwTfbFg4+rqRGPN4WTec+2haulf2JLqQtZFwMavfsoV2VmweG2BgLGUNsNLrrV0CvxxAVgSHsHipff/TBRZ8L+7dTjAdKnQIqCSHKYXQUfYH+D8lsBd4EjgOvA/seN/8B/94eSGEJAt4SQtgDCCFcpZRJwG0hRC9TmBBCPL6GNvHt8tXUq9+OevXbsXXrLgYNeB2Ahg3qkpSYZDF8BRAREUVyUjING9QFYNCA1/njj13m+Datm3LtWjChodnDXPfuhdKyxSsA2Nvb0bBhXa5dC36sXtX93bkbk0RoXDJanZ5dF27TvKq/hYxPaQf+umks51ZUAlk6PS6lbAmNS0ZnGpoIi08hJDoRX5eitf7uX7iJe1lvXPw9UFupqd2lEZeDzljI+FYvS89577D6ncWkxiaZw9eOXcr8V0azoMn7/DnvZ85sOlxo5wEQdeEWzuW8cQzwQGWlpmK3l7kTdNZCxqmcl/lzmdaBJN02OnXHAA+EafjOwc+N0hV8SXloKLCgpF64gU1ZH6wDPBFWGly6NiUxKHtYxpCcxsXag/in8TD+aTyM1HPXLJwHQuDy6ivEby26A4m6cAvnstm2qND1ZUIesoVzWUtbJIY8whYVfUkugi10N66i8vFH5ekNGg3WTVqhPXXUQkb71xGsahjbc8LRGZVvAIbIsLyy+5+hMHMgj8M0pzEK2IVx5eoGKeU/QojZQoiuJrEfADchRDAwHsi11Pdh/q09kEIhpdwphAgETgshsoDtwFRgAPCtEGIaYAWsAy4UJu/tO/bSoUMrrl05Slp6Ou+8M94cd/rUburVN84xjBo91byMd+eu/ezYuc8s17t3N/Pk+QOWfbuKH77/ggvn9yGEYPXq9Vy6dIXHTdFo1Comd23Iuz/uwSANdKtXiYpeLiwLOkc1PzdaVHuB8Z3qMfv3Y6w5chkEfPz6KwghOBcSxY8HL6FRq1AJwZRuL+NSyrYwpjBj0BvYMmMV7/x3Ciq1ilMbDhB54z7txr3O/Uu3ubznDJ2n9Mfa3paBy8YAkBAay6qhxbfyReoNHJm+mk5rPkCoVFxbf5D466HUm9iT6Au3uRN0lhqD2+HXpDoGnZ7MxFT2j/sOAO8GLxI4sgsGnR5pkBz5aBUZ8Y9fwPBI9AbuTV9BxZ9nIdQqYtfvJeP6PXwm9CftYrCFM8kLh4bV0YbFkHU3smjlk22Lzj//X3tnHmVZVZ3x39dFKw00IAtiCGGWUWxooMMYhBBI0EAUUSEMCWgg6mJGUAwBdDHGKAbFRQhgg8pkREEBQWimMDRNd9sM0jImgBhoBmnmpvrLH+e8qtePV0OXfc+9Re3fWm9R91YV++Px6u5z9tnDsain7b04+hM8N2eI92LK+kxuey9uG+l7sbCX1847i4knfj2l8d54Db1PPsGEfQ7i7UceYsE9d7Bg1nTGbzaFFf59Kl64kNenfhfPT4uLiaecTc9qa6ClJ7DieVfw6nfOZMHse0b8ngzEF088nXtmzeGll15m54/tx+c/sz+f2P2vlrid4bIkB0rZvob07Gu/9y9tX78BfHJx/p1q+sSrJtEKYdXJ/Eu/ULcEAE486r66JTRmIuEUza9bQnMmEm755NA/VDFNmUg4fuV1/oBcxsRKE9cb9jPnhfkP/8H2FpcxsQMJgiAYjTR9gR8OJAiCoKHESNsgCIJgRPQujIFSQRAEwQiIdu5BEATBiGh6O/dwIEEQBA0lDtGDIAiCEREhrCAIgmBELIxD9CAIgmAkNHv/EZXoxZF0cG7QOOZ1NEFDU3SEhmbpaIKG0cBYaabYJA4e+keK0AQdTdAAzdARGvppgo4maGg84UCCIHe8GocAAA8wSURBVAiCEREOJAiCIBgR4UDK05S4ahN0NEEDNENHaOinCTqaoKHxxCF6EARBMCJiBxIEQRCMiHAgQRAEwYgIBxIEQRCMiHAgFaLEVpL2zK+tJBUfO9kUJPVI+kHN9qfVZT8I3m2EA6kISbsCDwMnAR/Jr5OBh/P3Suu5eDj3qsR2L7CmpPeUtNthf6GkFeqwPxCSlpe0UutVg/1JkvZoW+jsWYOGv5E0S9ILkl6WNF/Sy4U1rC/pRkn35+tJkv65pIbRRmRhVYSkXwO72X6i4/7awDW2NyqsZ6btzduue4D7bG9cWMdFwEbAVcCrrfu2v1HI/k+BycANHfYPK2G/Q8shpEXFG/S3PbLtdQpquACYBDwAtDr32fZBpTRkHY8Ae5I+k7U8lCTdAnwRONf25Hzvftub1KFnNBDNFKtjKeCpLvefBsaXEiHpy8DxwIS2FZ2At6gn1/3R/BoHTKzB/o/zqwkcA2xie16NGrYuvYgYgCeB++tyHpllbE/viDK/XZeY0UA4kOq4ALhH0qWkPw6A1YG9gfML6njE9kRJl9v+VEG7XbF9MoCk5fL1K4XtT80htPXzrbm2F5TU0MajwGs12W5xp6SNbT9Ys45jgWvyLuDN1s1SO9PMPEnrkneDkvYCnilof9QRIawKkbQR8LfAavnW08BVJf9YW6GrzhBWXUjaBLgYaMX65wEH2H6gkP0dganAE6Sd2OrA39u+tYT9Di2TgQuBu1n0oVksnCbpw6Rw4u+yBiUJnlRKQ9ZxPfAKcB/9obS+BUchDeuQduXbAi8CjwP7dYahg37CgbzLkXQDaUU1Bbit8/u29yis5w7gK7an5esdgVNtb1vI/r3A39mem6/XBy6xvUUJ+x1apgO3886H5tSCGh4Bjuqi4X9Kacg6GnPWIGlZYJzt+XVraToRwnr381Fgc9Kq/99q1gKwbMt5ANi+Of/BlmJ8y3lk+7+RVOxMqouWo2qy3eI521fVrAFS+GpX29fXJUDSqcCZtl/K1+8DjrYdmVgDEDuQMYKkVWw/1wAdVwIzSQ4NYD9gC9sfL2T/AtJK+/v51r5AT+mso6zlVFIo7WoWDWG9UFDDOcCKXTQUTTSQNB9YlpTc0TqTsu3lC2qY1cq+arvXiNBvUwkHMkaQdDWDTMgsFcrKq7qTge3zrduAk2y/WMj+e4EvdNg/x/abA/9WZVoe73K7dBrvhQNoKO5Q60bSHGBK67MgaQIww/YH61XWXMKBFKBzPGYd4zIlfQv4Y/pX3vsA/wf8BMD2LYX1TExmy2ZhZdvvATYgOdQ6s7CCNiTtAeyQL2+2/bPC9o8DdiclNgAcSEp6ObOkjtFEnIGUobN9SR3tTLazvWXb9dWSZtg+sqQISR8CLiJnYUmaR8qCur+Q/R3pyMKSVFcW1njgc7Q9NElFbMUcmqQ/Bc4Gtsu3bgMOt92thqlKHaeTEj1arW4Ol7Sd7S+X0mD7jLwL2Tnf+prtX5SyPxqJHcgYIVfGf9T2Y/m6ror4yMLq1/KfpKLSVtbV/kCv7c8W1HAD8EMWPZPa1/YupTRkHXOAzWwvzNc9wKzS6cTB4hE7kIqQNGh2TeECKYAjgZslPZav1wIOLqwBIgurnSm2N227vknSrwprWMV2+znI9yQdUVhDixWBVgJBsX5lkm63vX0+yG9fUbdqYood5I82woFUR6tNxwakrXkrVXJ3YHopEZKmAE/avk7SesA/kbbo1wMzSulo4zFJJ7DoivexQX5+STMjr/zbs7DqeB8AeiWta/tR6Ctk6y2s4XlJ+wGX5Ot9gOcLawA4DZil1C1ZpLDel0oYtr19/mcdrXVGNRHCqhhJt5JCR/Pz9UTg57Z3GPw3l5j9mcBf2n5B0g7ApcChwGbARrb3KqGjTU9kYfVr2Zl0YPsY6aG5JnBg+w6tgIY1SWcg2+Rb/w0cZvt/S2lo07IqabEFMN327wra7gEesL1hKZvvBsKBVIykucCkttTA9wJzbG9QyP6vWmESSd8hFY6dlK9n296shI6gO/nz0PoszK3DkTWFjiysW2xfXdj+T4FD63Ceo5UIYVXPRcD0XEAH8DH6D01L0CNpKdtvk0JX7ecexf7/112HIum+IewXP6zNZy+H0JaFJSmysBKHSdrG9vEFZbwPeCC3mGlv9V+03c9oInYgBZC0OfDn+fJW27MK2v4KaZjVPGANYHPblvQBYKrt7Qb9Fyw5HR8e7PtV16HkUM1g9ov2foLIwurQUXsW1kCf0dI1UqOJ2IGUYRngZdsXSlpF0tq2u1UhL3FsnyLpRmBV4Hr3rxjGkc5CSvF4zaGBVW3fVaP9bkQW1qLUlYW1NCm55AOkppLn5x17MAQx0rZiJJ0IHAe0CqLG058BVATbd9m+0nb7tvw3tmcWlPGT1heS/qug3RbntNm/swb73ehVmj8B1JuFpTQvvidnZNWRhXUqKQvre5KmAvcCpxSyPRXYkuQ8dqMZTUdHBbEDqZ6Pk0aozgSw/duciTXWaK++L9braQD7S9dgvxvHANNybU5fFlZhDQeRzkC+STojugP4h5ICJI0jNbjcmv4srOMKZmFtbPtDWcv5FEyzH+2EA6met/KZQ2vKWcmiuSbhAb4uxbicQjyu7es+p1KyAy70xfg3BdajxiysfPbTd0ic35fPU271j+2Fko61fTn99VIl6UtasP22VEenodFJHKJXjKRjSA+JXUjFUgcBP7R9dq3CCiOpl5TZImAC/aNci1T7SnqCtMrt9nQo2gG3haTptv+stN1se3XgBOBPgCtJ9UEnAweQWrscXljP6aREj8tYNAOqcsfe9tmERT+fUYk+BOFACiBpF2BX0gfyF7ZvqFlS0AAkfZN0Jtb50Kz8bCpXfN8C3An8dX7NBo4sWcDXpqf21vbB4hMOpBCSlqctZFg6ZDLWyanUA1I4oQDoe4h3keK/KGC7r8A0Xz8FrNFKow2C4RBnIBUj6RBSaOAN+kMopp6D5LHMYJk1Bip/aL/DqL1TaZvtdJwDPQ+soHwAUMcCR9K2pCaf7Quti0rrCIZP7EAqRtLDwDa259WtJWgGTejU3LQzIUkXA+uSwmitVGbbPqykjmDxiB1I9TxK/4Fx0AAkbQJsTFs6b+GVbu2dmm2vVcLOYrAlKZ02VrSjiNiBVIykyaSOq3cDfSmasbKqh1zYuSPJgVxDKhy7vXRX4qyl1k7NTULSFaQuwM/UrSUYPrEDqZ5zgZtIVa5xQFk/e5HqL2bZPlDS+yncGaCN9wNvtV2/le/ViqSZtgdNOliCtlpNNicCD+ZGhu0LrWhk2GDCgVTPeNuDxryDoryeC9fezplxzwKr16Sl7k7NXSnlPDJfL2grWMKEA6meayUdDFzNoiurSOOthxmSVgTOI/VbeoVUC1Gc3OjyWvo7NR9YslNzE2h1upV0hu3j2r8n6QxSrUrQUOIMpGKiQKq5SFoLWN72nBo1bA+s1+rUDCxXqlNztt85Bxzg96Qxv0fbLjJuuFvYTNKcOua0BMMndiAVY3vtujUE/Ui60fbOALaf6LxXWMuJpOyjDUiJFq1OzUVmtGTOAp4izQQRsDcpnXYmcAEp4aAyJH2O1HtrnTwTpMVEUmPHoMHEDqQADUgbHfPkmQ/LANNID8VW/cPywHV1zMKWNJvcqdn25Hyv6Kq7syK9pcv2Zt2+V4H9FUiTAE8DvtT2rfkR5m0+sQOpmIHSRkkHqEE5DgGOIDUPbG9b8jLw7VoUNaNT82uSPgX8KF/vReqaAAW6Jtv+PSlktg+ApD8iLbSWk7RczCdvNrEDqZg8i7uVNrppK2209MjQICHp0KZ0Qm5Cp+Y8xOpbwDYkh3EXcCTwNLCF7dsL6dgd+AbJwT9Lmo3ya9sfLGE/GBnhQCqm1bJb0r3ATsB80h9G8ZBJAJLeQxpf2irWuxk41/aCAX+pWj3RqZkUSiP1I/ul7cmSdgL2s/2ZmqUFgxAhrOppTNpoAKTRtuPpH3G7P/Bd4LN1iMkO4wZJK1PDKNmc+fWPvLOJ4UGFpSyw/bykcZLG2Z4m6azCGoLFJHYgBWlC2uhYRdJSedpct0Pjyg+LO+xtDZwOvAB8DbgYWJk0LfEA29cV1HIHcBtpcdM3j9120bn1kn5JKqQ8jfRePAtMsb1tSR3B4hEOpACSViPFdNtXeLfWp2js0aozkDQT+KTtR/P9dYAflay+ljQDOB5YAfgPYDfbd0nakDQNcHJBLbNtb1bK3iA6lgVeJznRfUnvzQ9sF9+VBcMnQlgVk6tpPw08SFubaiAcSFlaabvHANMktQrk1gIOLKxlKdvXA0j6qu27AGw/VMM87p9J+ojta0obbsd2ayLjQkk/B56PzrzNJ3YgFSNpLjDJ9ptD/nBQGXniXmvOxgSgJ3/dS+qPVfkMjjYtfVXXnRXYJRsZZnvzgWVJbXYWUHgOeJPCecHiEzuQ6nmMdGgbDqReeoDleOcApaXon89Rik0lvZy1TMhfk6+XHvjXljy2S/+3d/Jt+sN5N9ERzgPCgTSYcCDV8xowW9KNxDyQOnnG9lfrFgFgu2fon6oWSRvmkFnX3U7BGfFNCucFi0k4kOq5iv6Jc0F9xNNoUY4CDqb7rPiSM+LbZ+S83kVH0GDiDCQYE0haKXorNQ9JvcCr5HAe/eOfBSxte3xd2oKhCQdSMZK2A06iP423dUgZ7dyD2skdcC8BLm+lNgfBcAkHUjGSHiL1Fuos1Ir89qB2JK1JSjP/NCmcdBnJmUQTw2BIwoFUjKS7bW9Vt44gGApJ6wEnAPs24aA/aD5xiF490yT9K/BjFs3CKpXlEgSD0rEL6QWOrVdRMFqIHUjFSJrW5bZtl8pyCYIBkXQ3qU7pCuCyUiNsg3cH4UCCYAwjaQPbc+vWEYxOwoFUhKSjOm4ZmAfcbvvxGiQFQR+S9rP9/S6fUwBKtnYJRi/j6hbwLmZix2t5YEvgWkl71yksCEj9r+Cdn9OJpJYvQTAksQMpjKSVSFPXijXMC4LFQdIRtmOYUzAksQMpTK6GjrYaQZPpGtYKgk7CgRQmz3p+sW4dQTAIscAJhkXUgVSEpPt4ZzO4lYDfAgeUVxQEwybi2sGwiDOQisjFWe2YNGXt1W4/HwQlyYOkuv3xC5hgOxaXwZCEAwmCIAhGRJyBBEEQBCMiHEgQBEEwIsKBBEEQBCMiHEgQBEEwIv4f6jtaF7hSL4wAAAAASUVORK5CYII=\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Training the data"
      ],
      "metadata": {
        "id": "qyUzXgX9qcQQ"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.model_selection import train_test_split"
      ],
      "metadata": {
        "id": "lPxBpjRSPZBK"
      },
      "execution_count": 30,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "X = df[['Unnamed: 0', 'Sqft', 'Floor', 'TotalFloor', 'Bedroom', 'Living.Room',\n",
        "       'Bathroom']]\n",
        "y = df[\"Price\"]"
      ],
      "metadata": {
        "id": "NzrMz1o5PY3c"
      },
      "execution_count": 32,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25,random_state=0)"
      ],
      "metadata": {
        "id": "s6wJWMf7PYgG"
      },
      "execution_count": 36,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Using the Linear Regresson model"
      ],
      "metadata": {
        "id": "HuvWWudMqhXR"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.linear_model import LinearRegression\n",
        "lr = LinearRegression()\n",
        "model = lr.fit(X_train,y_train)"
      ],
      "metadata": {
        "id": "A3T7kiJKPYLy"
      },
      "execution_count": 93,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Predicting the data"
      ],
      "metadata": {
        "id": "14EcExHJqnKN"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "y_pred = lr.predict(X_train)\n",
        "y_pred\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "LPqCwsd6PT2X",
        "outputId": "1cd16afc-c7a0-421f-bee7-63568839e55c"
      },
      "execution_count": 48,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([ 33778.57638814,  29430.16587249,  31900.8890849 ,  88196.06329945,\n",
              "        90451.25828805,  81348.59481344,  86049.58360025,  80811.88964203,\n",
              "        38377.72005131,  53573.82635521,  67634.65340457,  68275.05117736,\n",
              "        45374.50156693,  34066.53062097,  42287.69049856,  59098.82925034,\n",
              "        26959.22305741, 115829.73268683, 120929.59261   ,  58637.00756946,\n",
              "        55877.50951676,  54474.2957368 ,  84198.0092373 ,  65566.07345107,\n",
              "        41893.67575508,  49335.81140449,  62158.71373371,  70844.57813901,\n",
              "        78632.82504223,  31166.16445499,  29612.83310903,  76195.84302472,\n",
              "        93430.80318904,  36278.08947208,  40185.56396287,  74156.77332983,\n",
              "       118339.64404027,  59544.35627432, 118569.80003828,  36413.0465475 ,\n",
              "        27376.27508649,  56940.18434532,  58158.79224159,  60421.00315787,\n",
              "        29625.38737008,  76492.95915698,  76208.50482056,  48176.56774122,\n",
              "        69311.09132272,  54786.26597937, 100845.72042089, 112264.02902452,\n",
              "        49449.21534918,  85017.38167895,  30308.19217816,  79449.26778859,\n",
              "        58672.4759446 ,  28348.73072706,  32320.547347  ,  63747.00440538,\n",
              "        35304.13059318, 152202.49236335,  76182.57355181,  25622.49149176,\n",
              "        33547.80332969, 145415.51646412,  58635.52190314,  88346.7301882 ,\n",
              "        88694.86823625, 165734.44724411,  28275.31412803,  60134.31646123,\n",
              "        41590.26536342,  45375.18640689,  50635.84897872,  28525.91359156,\n",
              "        25509.41290428,  56617.15080167,  63361.11373516,  51432.67642827,\n",
              "       111806.83606909,  49568.42302365,  48181.1501184 ,  80590.35819012,\n",
              "        87614.17028118,  43518.18430595,  88597.70856868,  56414.15676734,\n",
              "        80645.47294513,  32210.29813959, 146800.50514777,  40693.80758955,\n",
              "        74179.70357415,  31576.73187829,  67505.16851114,  26444.45940268,\n",
              "        35987.73308136,  34995.95209505,  33797.76015812,  77112.06893214,\n",
              "        76537.159704  ,  82797.92386411, 115904.89073505,  25576.97059189,\n",
              "        57348.30322871,  69635.56630715,  58312.43532604,  55306.94532905,\n",
              "        40967.2678368 ,  67936.76426345,  69672.01817184,  41035.92202905,\n",
              "        42100.94381569,  29072.74386829,  54259.3940287 , 132999.66130326,\n",
              "        46525.2774657 , 172321.44290999,  72585.90550388,  90611.57164557,\n",
              "       127782.74473591,  69319.94525737,  76456.61287276,  59183.61185435,\n",
              "        33228.71917909,  31041.18785934,  51588.42946815,  57444.62247581,\n",
              "        60744.17352273,  43618.835788  ,  81598.26752709,  62905.42114676,\n",
              "        44534.97165428,  77015.25764484,  87160.95894216, 168359.12736105,\n",
              "        16298.25160027,  34720.23574603,  64865.94193162,  64085.03999233,\n",
              "       161053.40446495, 106512.24483457,  49336.81274101,  51130.59533759,\n",
              "        85412.89767815,  79004.86827413,  41577.71390175,  50249.61588852,\n",
              "        53929.03520842,  58413.11536322,  41482.78900124,  29603.09536878,\n",
              "        57163.34118794,  48761.31874211, 104012.81287124,  48889.9361269 ,\n",
              "        30144.42982028,  55586.63301508,  49695.11079214,  20341.96734389,\n",
              "        70918.07350911,  75191.12271267,  98275.64029344,  53277.93806497,\n",
              "        48872.1937158 ,  39680.65181553,  73288.90836873,  77566.41533642,\n",
              "        75300.79610294,  36633.17470302, 103226.18383769,  51845.63691112,\n",
              "        77833.86419794,  51042.08940517,  95543.23413921,  75216.08621141,\n",
              "        55069.54491983,  27033.69434967,  50534.39213979,  46432.08780831,\n",
              "        36950.67361419,  81538.36211877,  39299.60047539, 112534.41578342,\n",
              "        50155.59575123,  20151.62893852,  56800.28867825,  39860.47528194,\n",
              "        39925.23268278, 104539.68351054,  35775.01949247,  38210.77114088,\n",
              "        57034.72082446,  75440.98113108,  26877.12941523, 123935.15868896,\n",
              "        49616.56592084,  75079.89566804,  43197.18245679, 130884.89949446,\n",
              "        32606.61852771,  45707.80886091,  68880.56835635,  22052.4419439 ,\n",
              "        33350.43518753,  69688.76136919,  18755.4160059 ,  86208.64607925,\n",
              "        79142.91114436,  83473.43440309,  26586.16530553,  34760.58095536,\n",
              "        60080.05877971,  34922.50368075,  39594.74181047,  30452.66927439,\n",
              "        32682.4485966 ,  75806.55603515,  37473.28368937,  31120.58811307,\n",
              "        42589.87951277,  26932.72433308, 122888.7248655 ,  81117.43145948,\n",
              "        27838.40130799,  39240.5065144 ,  88801.99923252,  53820.32853187,\n",
              "        48527.31152877,  35709.14508365,  90308.49609101,  35506.13447739,\n",
              "        80663.29035821,  96948.76404087,  67951.04518111,  29066.41332782,\n",
              "        70423.86094834,  61172.37222907,  54216.2726667 ,  16506.28901256,\n",
              "        38617.37162751,  26713.99646341,  69920.62315367,  28656.29978774,\n",
              "        31975.60003595,  67133.61685054,  58220.40804322,  53082.19356229,\n",
              "        80932.05360055,  29792.57877052,  27473.86400337,  51194.13799532,\n",
              "        51587.59379315,  36411.29245494,  51743.89068659,  85204.07435307,\n",
              "        77916.67582126,  49771.01425012,  35720.02943417, 226760.32823471,\n",
              "        33939.51671128,  32498.89433358,  78727.5382453 ,  47806.42202895,\n",
              "        53327.61600019,  72025.79985507,  27561.76953297,  58507.70507242,\n",
              "        73038.24484387,  77024.30489639,  31200.83027528,  31636.48543155,\n",
              "        32817.31529305,  61438.39760235,  39909.30774901,  49046.07392198,\n",
              "        53922.65190769,  32331.54775507,  77019.36995916,  71174.57997261,\n",
              "        29342.61042326, 112700.24044172,  30281.36486286,  56341.06387541,\n",
              "        38864.3177395 ,  50088.33033053, 118450.33545281,  35937.04990386,\n",
              "        59798.51348958,  66791.1511796 ,  23756.82933676,  59575.22181455,\n",
              "        40602.82861079,  27700.59031413,  50647.01964609,  41780.53078949,\n",
              "        68479.51702065,  50057.19394815,  37644.39821611,  79805.96517855,\n",
              "       143120.11222598, 135867.65984636,  64246.41412715,  47968.55319524,\n",
              "        52431.85800358,  54696.95455433,  41973.9326124 ,  97972.13137156,\n",
              "        79563.71471825, 117926.0275932 ,  44546.11106278,  46781.20639731,\n",
              "        82831.79721493,  67311.2481645 ,  50473.55281755,  77062.89909188,\n",
              "        53936.02617074,  34159.91185592,  57294.61271051,  67006.71017966,\n",
              "        58678.90978801,  49144.62354138,  22914.35836222, 165753.71085694,\n",
              "        65938.34299716,  61210.19154081,  79650.80874404,  65213.09325542,\n",
              "        39704.52372979,  37904.36158079,  35398.13116787,  35267.3740203 ,\n",
              "        70016.94121783,  33663.50965888,  44835.88204892,  52276.10957789,\n",
              "       142643.66748801,  43933.55699293,  61720.85257959,  35082.51360867,\n",
              "        25490.67889512,  48168.16001943, 128401.50988204,  35498.08575482,\n",
              "        77451.84041425, 163152.66189534,  58408.65742792,  59149.31429462,\n",
              "       113428.38760898,  82153.94368107,  96171.98793454,  78327.77594802,\n",
              "        34811.51012893,  43242.14179476,  76910.87646807,  84998.11806612,\n",
              "        67460.74570046,  65149.00230575,  52738.64776735,  56124.77632799,\n",
              "        46184.15492383,  98083.86064945,  48900.85504934, 129169.72485969,\n",
              "        48750.68008524,  31970.77607669,  45102.07869507,  28916.8764546 ,\n",
              "       118322.95416953,  58175.75303556,  42450.69425945,  84532.18139994,\n",
              "        59792.96089546,  29509.07890139, 149500.20809614,  64133.91865474,\n",
              "       131444.15797475,  55465.63069772,  29531.54091425,  62027.6466662 ,\n",
              "        57020.11348691,  39589.18693883, 129805.42408309,  93664.32862684,\n",
              "        61100.77526197,  65250.91078315,  32800.03577235,  48191.24783866,\n",
              "       128883.02984973,  21617.6742277 ,  24953.34798754,  48983.80248758,\n",
              "        35746.12407322,  58518.57624598,  51981.40521539,  83311.86149392,\n",
              "        82794.36407067,  61605.53794646,  63662.26078351,  67550.36460845,\n",
              "        80649.52871021,  99791.29165773,  29332.8026415 ,  34780.90077488,\n",
              "        56314.4914268 ,  64080.48240119,  32107.93501025,  42279.82691704,\n",
              "        39844.74032743,  81428.50349731,  33312.95754719,  36187.83520323,\n",
              "        67929.2626645 , 100670.76924271,  54890.53218502,  50228.78952115,\n",
              "        63984.58774273,  54481.86871874,  33104.74023459,  47464.0230602 ,\n",
              "        70803.02292648,  57185.9366873 ,  89673.53110655,  39557.89344778,\n",
              "        28474.24323714,  53269.82432572,  62637.94166467,  58871.08009812,\n",
              "        80450.6841283 ,  35277.23325185,  68940.27657929,  39427.96272763,\n",
              "        39993.98000337,  54050.23809589,  50309.6102124 ,  51411.14656546,\n",
              "        66804.06613004,  76629.98538823,  46045.47340348,  57674.47234049,\n",
              "        41979.27693677,  30051.03852627,  72280.65592324,  55829.96599245,\n",
              "        34592.42329837,  32864.4247907 ,  49844.81881885,  26564.5137756 ,\n",
              "        43440.57645302,  49195.57104808,  86362.0354472 ,  77000.57212911,\n",
              "        92730.46876542,  56667.15646087,  57433.1090825 ,  39739.85148364,\n",
              "        42960.64284651,  90327.90587007, 197365.53225301,  46482.59314004,\n",
              "        80373.62967697,  62567.45324918,  92854.03636761,  64767.44598946,\n",
              "        72179.90875771,  52006.00970942,  88574.6921652 ,  34148.2283864 ,\n",
              "        72570.24182124,  65397.04062415,  34907.34462356,  59159.82539252,\n",
              "        72840.3457785 ,  40372.91702608,  63533.69966128,  44620.13308774,\n",
              "        76742.0390443 ,  71061.81935424,  55111.74087518,  79842.10870431,\n",
              "        97069.43320309,  58102.8656859 ,  36089.4766469 ])"
            ]
          },
          "metadata": {},
          "execution_count": 48
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Creating a DataFrame for better understanding the actual adn predicted data"
      ],
      "metadata": {
        "id": "v4Ly-EFqqscr"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "predicted_dataframe = pd.DataFrame({\"Actual_data\" : y_train , \"predicted_data\" : pred})\n",
        "predicted_dataframe"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 424
        },
        "id": "6qXGIINeVDZ1",
        "outputId": "34b2a6f8-0e3c-4ef3-ff5e-2cc3068a5fa5"
      },
      "execution_count": 92,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "     Actual_data  predicted_data\n",
              "118        22000    33778.576388\n",
              "235        36000    29430.165872\n",
              "449        36000    31900.889085\n",
              "175        82000    88196.063299\n",
              "356        55000    90451.258288\n",
              "..           ...             ...\n",
              "9          65000    55111.740875\n",
              "359        98000    79842.108704\n",
              "192        75000    97069.433203\n",
              "629        45000    58102.865686\n",
              "559        35000    36089.476647\n",
              "\n",
              "[483 rows x 2 columns]"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-2b8dca35-4e1b-4425-bed6-77ca3e44fc6f\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Actual_data</th>\n",
              "      <th>predicted_data</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>118</th>\n",
              "      <td>22000</td>\n",
              "      <td>33778.576388</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>235</th>\n",
              "      <td>36000</td>\n",
              "      <td>29430.165872</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>449</th>\n",
              "      <td>36000</td>\n",
              "      <td>31900.889085</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>175</th>\n",
              "      <td>82000</td>\n",
              "      <td>88196.063299</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>356</th>\n",
              "      <td>55000</td>\n",
              "      <td>90451.258288</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>9</th>\n",
              "      <td>65000</td>\n",
              "      <td>55111.740875</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>359</th>\n",
              "      <td>98000</td>\n",
              "      <td>79842.108704</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>192</th>\n",
              "      <td>75000</td>\n",
              "      <td>97069.433203</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>629</th>\n",
              "      <td>45000</td>\n",
              "      <td>58102.865686</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>559</th>\n",
              "      <td>35000</td>\n",
              "      <td>36089.476647</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>483 rows � 2 columns</p>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-2b8dca35-4e1b-4425-bed6-77ca3e44fc6f')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-2b8dca35-4e1b-4425-bed6-77ca3e44fc6f button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-2b8dca35-4e1b-4425-bed6-77ca3e44fc6f');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 92
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        ""
      ],
      "metadata": {
        "id": "U0IIAeKolPPk"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        ""
      ],
      "metadata": {
        "id": "mU3W7cHIlPOY"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        ""
      ],
      "metadata": {
        "id": "08lgbfZ0lPNC"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        ""
      ],
      "metadata": {
        "id": "0kI7grOdlPLQ"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        ""
      ],
      "metadata": {
        "id": "x1XoZx8DlPJ7"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        ""
      ],
      "metadata": {
        "id": "8ya9qZvOlPIZ"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        ""
      ],
      "metadata": {
        "id": "E_DkX1COlPHL"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        ""
      ],
      "metadata": {
        "id": "Q0A_fuVSlPFp"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        ""
      ],
      "metadata": {
        "id": "k_Y6h2cYlPEf"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        ""
      ],
      "metadata": {
        "id": "8jR4dkowlPCs"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        ""
      ],
      "metadata": {
        "id": "cqjH5tpNlPBg"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        ""
      ],
      "metadata": {
        "id": "WWB2eHZ-lO_x"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        ""
      ],
      "metadata": {
        "id": "2ZElb7--lO-e"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        ""
      ],
      "metadata": {
        "id": "btea_q83lO8v"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        ""
      ],
      "metadata": {
        "id": "6zElRvQ6lO7V"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        ""
      ],
      "metadata": {
        "id": "ksln0ni8lN-y"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        ""
      ],
      "metadata": {
        "id": "-VVsShO0lOA5"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        ""
      ],
      "metadata": {
        "id": "AHBxv2HclOBz"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        ""
      ],
      "metadata": {
        "id": "rBpacwrglODG"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        ""
      ],
      "metadata": {
        "id": "s4lkMPVSlOEj"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        ""
      ],
      "metadata": {
        "id": "lbS5VqAllOF2"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        ""
      ],
      "metadata": {
        "id": "CeQ1qmlilOHM"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        ""
      ],
      "metadata": {
        "id": "8E3LgajDlOIw"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        ""
      ],
      "metadata": {
        "id": "R5y23wnvlOJ6"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        ""
      ],
      "metadata": {
        "id": "99387GEYlOLT"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        ""
      ],
      "metadata": {
        "id": "1X1R_O7blONk"
      },
      "execution_count": null,
      "outputs": []
    }
  ],
  "metadata": {
    "colab": {
      "collapsed_sections": [],
      "name": "House rental prediction",
      "provenance": []
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}