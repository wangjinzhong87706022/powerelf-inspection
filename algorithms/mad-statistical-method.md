# MAD 统计异常检测

## 原理

MAD（Median Absolute Deviation，中位数绝对偏差）是一种鲁棒的统计离群点检测方法。相比 Z-Score（使用均值和标准差），MAD 基于中位数和 MAD，对异常值不敏感。

## 公式

```
MAD = median(|x_i - median(x)|) × 1.4826

M_i = 0.6745 × (x_i - median(x)) / MAD

若 M_i > threshold，则为异常
```

- `1.4826`：归一化因子，使 MAD 在正态分布下等价于标准差
- `0.6745`：归一化到标准正态分布的分位数

## 默认阈值

| 传感器 | 阈值 | 窗口(天) |
|--------|------|---------|
| 水位(rz) | 3.0 | 7 |
| 雨量(p) | 5.0 | 30 |
| 渗压(water_pressure) | 4.0 | 30 |
| GNSS位移(wgs84_delta_h) | 3.5 | 90 |
| 流量(inq/otq) | 4.0 | 30 |

## 算法步骤

1. 从传感器表读取指定窗口内的数值序列
2. 去除空值（`pd.to_numeric + dropna()`）
3. 计算中位数、MAD、归一化因子
4. 对每个数据点计算 Modified Z-Score
5. > threshold 的标记为异常
6. 返回异常点索引、Z-Score 分布、统计量

## Python 实现

```python
import numpy as np

def detect_anomalies(values, threshold=4.0):
    median = np.median(values)
    abs_devs = np.abs(values - median)
    mad = np.median(abs_devs) * 1.4826

    if mad == 0:
        # 退化到绝对差判断
        anomalies = [i for i, v in enumerate(values) if abs(v - median) > 0]
        z_scores = [0.0] * len(values)
    else:
        z_scores = 0.6745 * np.abs(values - median) / mad
        anomalies = np.where(z_scores > threshold)[0].tolist()

    return {
        "median": median,
        "mad": mad,
        "anomaly_count": len(anomalies),
        "anomaly_indices": anomalies,
        "z_scores": z_scores.tolist(),
    }
```

## 注意事项

- MAD=0 时（所有值相同），退化为绝对差判断
- 数据点 <10 时数据不充分，不做检测
- 窗口大小的选择影响结果：太小则样本不足，太大则对近期变化不敏感
