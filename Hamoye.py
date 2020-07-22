>>> A=[1,2,3,4,5]
>>> B=[13,14,15]
>>> A.extend(B)
>>> print(A.extend(B))
None
>>> A=[1,2,3,4,5,6]
>>> B=[13,21,34]
>>> print(A.extend(B))
None
>>> import numpy as np
>>> np.identity(3)
array([[1., 0., 0.],
       [0., 1., 0.],
       [0., 0., 1.]])

>>> import pandas as pd
>>> user=pd.read_csv('https://raw.githubusercontent.com/WalePhenomenon/climate_change/master/fuel_ferc1.csv')
>>> user.describe()
       utility_id_ferc1  ...  fuel_cost_per_mmbtu
count      29523.000000  ...         29523.000000
mean         118.601836  ...            19.304354
std           74.178353  ...          2091.540939
min            1.000000  ...           -41.501000
25%           55.000000  ...             1.940000
50%          122.000000  ...             4.127000
75%          176.000000  ...             7.745000
max          514.000000  ...        359278.000000

[8 rows x 7 columns]

record_id                       f1_fuel_1994_12_1_0_7f1_fuel_1994_12_1_0_10f1_...
utility_id_ferc1                                                          3501482
report_year                                                              59217412
plant_name_ferc1                rockportrockport total plantgorgasbarrychickas...
fuel_type_code_pudl             coalcoalcoalcoalgascoalnuclearcoalcoalcoalgasc...
fuel_qty_burned                                                       7.74128e+10
fuel_mmbtu_per_unit                                                        250713
fuel_cost_per_unit_burned                                             6.15995e+06
fuel_cost_per_unit_delivered                                          2.70894e+07
fuel_cost_per_mmbtu                                                        569922
dtype: object

>>> user.fuel_mmbtu_per_unit
0        16.590
1        16.592
2        24.130
3        23.950
4         1.000
          ...
29518     1.059
29519     1.050
29520     1.060
29521    16.108
29522     1.059
Name: fuel_mmbtu_per_unit, Length: 29523, dtype: float64

>>> user.fuel_mmbtu_per_unit
0        16.590
1        16.592
2        24.130
3        23.950
4         1.000
          ...
29518     1.059
29519     1.050
29520     1.060
29521    16.108
29522     1.059
Name: fuel_mmbtu_per_unit, Length: 29523, dtype: float64
>>> user.fuel_mmbtu_per_unit.describe()
count    29523.000000
mean         8.492111
std         10.600220
min          0.000001
25%          1.024000
50%          5.762694
75%         17.006000
max        341.260000
Name: fuel_mmbtu_per_unit, dtype: float64
>>> user.fuel_cost_per_unit_burned
0        18.59
1        18.58
2        39.72
3        47.21
4         2.77
         ...
29518     4.78
29519     3.65
29520     4.77
29521     3.06
29522     0.00
Name: fuel_cost_per_unit_burned, Length: 29523, dtype: float64
>>> user.fuel_cost_per_unit_burned.describe()
count     29523.000000
mean        208.649031
std        2854.490090
min        -276.080000
25%           5.207000
50%          26.000000
75%          47.113000
max      139358.000000
Name: fuel_cost_per_unit_burned, dtype: float64
>>> user.fuel_cost_per_unit_burned.min()
-276.08

>>> user.fuel_qty_burned.skew()
15.851495469109503
>>> user.fuel_qty_burned.kurt()
651.3694501337732
>>> user.isnull()
       record_id  ...  fuel_cost_per_mmbtu
0          False  ...                False
1          False  ...                False
2          False  ...                False
3          False  ...                False
4          False  ...                False
          ...  ...                  ...
29518      False  ...                False
29519      False  ...                False
29520      False  ...                False
29521      False  ...                False
29522      False  ...                False

[29523 rows x 11 columns]
>>> user.isnull().describe()
       record_id  ... fuel_cost_per_mmbtu
count      29523  ...               29523
unique         1  ...                   1
top        False  ...               False
freq       29523  ...               29523

[4 rows x 11 columns]
>>> user.isnull().max()
record_id                       False
utility_id_ferc1                False
report_year                     False
plant_name_ferc1                False
fuel_type_code_pudl             False
fuel_unit                        True
fuel_qty_burned                 False
fuel_mmbtu_per_unit             False
fuel_cost_per_unit_burned       False
fuel_cost_per_unit_delivered    False
fuel_cost_per_mmbtu             False
dtype: bool
>>> user.isnull().max().describe()
count        11
unique        2
top       False
freq         10
dtype: object
>>> user.describe()
       utility_id_ferc1  ...  fuel_cost_per_mmbtu
count      29523.000000  ...         29523.000000
mean         118.601836  ...            19.304354
std           74.178353  ...          2091.540939
min            1.000000  ...           -41.501000
25%           55.000000  ...             1.940000
50%          122.000000  ...             4.127000
75%          176.000000  ...             7.745000
max          514.000000  ...        359278.000000

[8 rows x 7 columns]
>>> user.fuel_cost_per_unit_delivered
0        18.53
1        18.53
2        38.12
3        45.99
4         2.77
         ...
29518     4.78
29519     3.65
29520     4.77
29521    14.76
29522     0.00
Name: fuel_cost_per_unit_delivered, Length: 29523, dtype: float64
>>> user.report_year
0        1994
1        1994
2        1994
3        1994
4        1994
         ...
29518    2018
29519    2018
29520    2018
29521    2018
29522    2018
Name: report_year, Length: 29523, dtype: int64

>>> user.isnull().corr()
                              record_id  ...  fuel_cost_per_mmbtu
record_id                           NaN  ...                  NaN
utility_id_ferc1                    NaN  ...                  NaN
report_year                         NaN  ...                  NaN
plant_name_ferc1                    NaN  ...                  NaN
fuel_type_code_pudl                 NaN  ...                  NaN
fuel_unit                           NaN  ...                  NaN
fuel_qty_burned                     NaN  ...                  NaN
fuel_mmbtu_per_unit                 NaN  ...                  NaN
fuel_cost_per_unit_burned           NaN  ...                  NaN
fuel_cost_per_unit_delivered        NaN  ...                  NaN
fuel_cost_per_mmbtu                 NaN  ...                  NaN

[11 rows x 11 columns]
>>> user.isnull().describe()
       record_id  ... fuel_cost_per_mmbtu
count      29523  ...               29523
unique         1  ...                   1
top        False  ...               False
freq       29523  ...               29523

[4 rows x 11 columns]

>>> user.isnull.__class__
<class 'method'>
>>> user.corr()
                              utility_id_ferc1  ...  fuel_cost_per_mmbtu
utility_id_ferc1                      1.000000  ...             0.006122
report_year                           0.093323  ...             0.010261
fuel_qty_burned                      -0.057447  ...            -0.001896
fuel_mmbtu_per_unit                  -0.066946  ...            -0.005884
fuel_cost_per_unit_burned            -0.037863  ...            -0.000437
fuel_cost_per_unit_delivered         -0.016414  ...            -0.000109
fuel_cost_per_mmbtu                   0.006122  ...             1.000000

[7 rows x 7 columns]

>>> user.fuel_cost_per_unit_burned.describe()
count     29523.000000
mean        208.649031
std        2854.490090
min        -276.080000
25%           5.207000
50%          26.000000
75%          47.113000
max      139358.000000
Name: fuel_cost_per_unit_burned, dtype: float64
