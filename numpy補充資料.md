# 一些numpy的補充資料

因為.ipynb的檔案有時候在GitHub上面無法載入，所以我把部分內容移到.md檔上面，使用上比較方便。

## numpy 有哪些 ufuncs？

想知道 numpy 有哪些 ufunc ，可以參考官網上面的連結：[Available ufuncs](https://docs.scipy.org/doc/numpy/reference/ufuncs.html#available-ufuncs)

## 統計相關函式

參考：[Statistics](https://docs.scipy.org/doc/numpy-1.12.0/reference/routines.statistics.html)

|函式|說明|
|:-|:-|
|[sum](https://docs.scipy.org/doc/numpy/reference/generated/numpy.sum.html)|總和|
|[mean](https://docs.scipy.org/doc/numpy/reference/generated/numpy.mean.html)|平均|
|[std](https://docs.scipy.org/doc/numpy/reference/generated/numpy.std.html)|標準差|
|[var](https://docs.scipy.org/doc/numpy/reference/generated/numpy.var.html)|變異數|
|min, max|最小值、最大值|
|[argmin](https://docs.scipy.org/doc/numpy/reference/generated/numpy.argmin.html), [argmax](https://docs.scipy.org/doc/numpy/reference/generated/numpy.argmax.html)|最小值的索引、最大值的索引|
|[cumsum](https://docs.scipy.org/doc/numpy/reference/generated/numpy.cumsum.html)|和的累計值|
|[cumprod](https://docs.scipy.org/doc/numpy/reference/generated/numpy.cumprod.html)|積的累計值|

## 亂數相關函式

參考：[Random Sampling (numpy.random)](https://docs.scipy.org/doc/numpy/reference/routines.random.html)

|函式|說明|
|:-|:-|
|[seed](https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.seed.html#numpy.random.seed)|設定亂數的種子|
|[permutation](https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.permutation.html)|隨機排列|
|[shuffle](https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.shuffle.html)|沿著 axis 0 的隨機排列|
|[rand](https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.rand.html#numpy.random.rand)|返回指定形狀的亂數，亂數值為[0,1]間的均勻分布|
|[randn](https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.randn.html#numpy.random.randn)|返回指定形狀的亂數，亂數值為mean為0，variance為1的高斯分布|
|[randint](https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.randint.html#numpy.random.randint)|使用離散均勻分布，返回指定形狀的整數亂數|
|[normal](https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.normal.html#numpy.random.normal)|返回指定形狀的亂數，亂數值為自訂的mean跟variance的高斯分布|
|[uniform](https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.uniform.html#numpy.random.uniform)|使用均勻分布，返回指定形狀的亂數|