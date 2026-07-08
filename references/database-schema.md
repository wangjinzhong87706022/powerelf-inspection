# 数据库 SQL 参考

## 水文气象监测表

### st_rsvr_r（水库水情）
```sql
CREATE TABLE st_rsvr_r (
    st_id    INT          NOT NULL COMMENT '测站ID',
    tm       DATETIME     NOT NULL COMMENT '采集时间',
    rz       DECIMAL(10,2) COMMENT '库水位(m)',
    inq      DECIMAL(10,2) COMMENT '入库流量(m³/s)',
    otq      DECIMAL(10,2) COMMENT '出库流量(m³/s)',
    w         DECIMAL(10,2) COMMENT '蓄水量(万m³)',
    blrz     DECIMAL(10,2) COMMENT '下游水位(m)',
    stcd     VARCHAR(20)  COMMENT '站码',
    PRIMARY KEY (st_id, tm)
);
```

### st_river_r（河道水情）
```sql
CREATE TABLE st_river_r (
    st_id    INT          NOT NULL COMMENT '测站ID',
    tm       DATETIME     NOT NULL COMMENT '采集时间',
    z        DECIMAL(10,2) COMMENT '水位(m)',
    q        DECIMAL(10,2) COMMENT '流量(m³/s)',
    xsa      DECIMAL(10,2) COMMENT '断面面积(m²)',
    xsavv    DECIMAL(5,2)  COMMENT '平均流速(m/s)',
    xsmxv    DECIMAL(5,2)  COMMENT '最大流速(m/s)',
    stcd     VARCHAR(20)  COMMENT '站码',
    PRIMARY KEY (st_id, tm)
);
```

### st_was_r（闸站水情）
```sql
CREATE TABLE st_was_r (
    st_id    INT          NOT NULL COMMENT '测站ID',
    tm       DATETIME     NOT NULL COMMENT '采集时间',
    upz      DECIMAL(10,2) COMMENT '上游水位(m)',
    dwz      DECIMAL(10,2) COMMENT '下游水位(m)',
    tgtq     DECIMAL(10,2) COMMENT '总过闸流量(m³/s)',
    stcd     VARCHAR(20)  COMMENT '站码',
    PRIMARY KEY (st_id, tm)
);
```

### st_tide_r（潮汐水情）
```sql
CREATE TABLE st_tide_r (
    st_id    INT          NOT NULL COMMENT '测站ID',
    tm       DATETIME     NOT NULL COMMENT '采集时间',
    tdz      DECIMAL(10,2) COMMENT '潮位(m)',
    airp     DECIMAL(10,2) COMMENT '气压(hPa)',
    tdptn    VARCHAR(10)  COMMENT '潮位状态',
    hltdmk   VARCHAR(4)   COMMENT '高低潮标记',
    stcd     VARCHAR(20)  COMMENT '站码',
    PRIMARY KEY (st_id, tm)
);
```

### st_flood_r（防洪区水情）
```sql
CREATE TABLE st_flood_r (
    fca_id   INT          NOT NULL COMMENT '防洪区ID',
    tm       DATETIME     NOT NULL COMMENT '采集时间',
    z        DECIMAL(10,2) COMMENT '水位(m)',
    q        DECIMAL(10,2) COMMENT '流量(m³/s)',
    PRIMARY KEY (fca_id, tm)
);
```

### st_pptn_r（雨量）
```sql
CREATE TABLE st_pptn_r (
    st_id    INT          NOT NULL COMMENT '测站ID',
    tm       DATETIME     NOT NULL COMMENT '采集时间',
    p        DECIMAL(5,1) COMMENT '时段雨量(mm)',
    dr       DECIMAL(6,1) COMMENT '时段长(分钟)',
    dyp      DECIMAL(5,1) COMMENT '日雨量(mm)',
    cump     DECIMAL(5,1) COMMENT '累计雨量(mm)',
    pdr      DECIMAL(5,5) COMMENT '降水历时',
    stcd     VARCHAR(20)  COMMENT '站码',
    PRIMARY KEY (st_id, tm)
);
```
> ⚠️ `dr` 单位是**分钟**，计算降雨强度需转换：`强度 = p / (dr/60)` mm/h

### st_pptn_region_r（分区雨情）
```sql
CREATE TABLE st_pptn_region_r (
    re_id    INT          NOT NULL COMMENT '区域编码',
    tm       DATETIME     NOT NULL COMMENT '采集时间',
    drp      DECIMAL(6,1) NOT NULL COMMENT '时段雨量(mm)',
    intv     DECIMAL(6,2) NOT NULL COMMENT '时段长(小时)',
    pdr      DECIMAL(6,5) NOT NULL COMMENT '降水历时(h)',
    dyp      DECIMAL(6,1) NOT NULL COMMENT '日累计雨量(mm)',
    wth      CHAR         COMMENT '天气',
    PRIMARY KEY (re_id, tm)
);
```
> ⚠️ `intv` 单位是**小时**，与 `st_pptn_r.dr`（分钟）不同

### st_pptn_dp_s（日雨量）
```sql
CREATE TABLE st_pptn_dp_s (
    st_id    INT          NOT NULL,
    dt       DATE         NOT NULL COMMENT '日期',
    dp       DECIMAL(5,1) COMMENT '日雨量(mm)',
    PRIMARY KEY (st_id, dt)
);
```

### st_pptn_mtp_s（月雨量）
```sql
CREATE TABLE st_pptn_mtp_s (
    st_id    INT          NOT NULL,
    mt       DATE         NOT NULL COMMENT '月份',
    mp       DECIMAL(6,1) COMMENT '月雨量(mm)',
    PRIMARY KEY (st_id, mt)
);
```

### st_pptn_yrp_s（年雨量）
```sql
CREATE TABLE st_pptn_yrp_s (
    st_id    INT          NOT NULL,
    yr       YEAR         NOT NULL COMMENT '年份',
    yp       DECIMAL(7,1) COMMENT '年雨量(mm)',
    PRIMARY KEY (st_id, yr)
);
```

### st_pptn_dcp_s（旬雨量）
```sql
CREATE TABLE st_pptn_dcp_s (
    st_id    INT          NOT NULL,
    tm       DATE         NOT NULL COMMENT '旬日期',
    dp       DECIMAL(6,1) COMMENT '旬雨量(mm)',
    PRIMARY KEY (st_id, tm)
);
```

## 设备工情监测表

### rei_gate_r（闸门）
```sql
CREATE TABLE rei_gate_r (
    st_id    INT          NOT NULL,
    tm       DATETIME     NOT NULL,
    gtq      DECIMAL(10,2) COMMENT '流量(m³/s)',
    gtophgt  DECIMAL(5,2)  COMMENT '开启高度(m)',
    gtopnum  TINYINT      COMMENT '开启孔数',
    status   TINYINT      COMMENT '闸门状态(1=开启/2=关闭/3=异常)',
    stcd     VARCHAR(20)  COMMENT '站码',
    slcd     VARCHAR(20)  COMMENT '闸码',
    PRIMARY KEY (st_id, tm)
);
```

### rei_pump_r（泵站）
```sql
CREATE TABLE rei_pump_r (
    st_id    INT          NOT NULL,
    tm       DATETIME     NOT NULL,
    uab      VARCHAR(10)  COMMENT 'AB相电压',
    ubc      VARCHAR(10)  COMMENT 'BC相电压',
    uca      VARCHAR(10)  COMMENT 'CA相电压',
    ia       VARCHAR(10)  COMMENT 'A相电流',
    ib       VARCHAR(10)  COMMENT 'B相电流',
    ic       VARCHAR(10)  COMMENT 'C相电流',
    p        VARCHAR(10)  COMMENT '有功功率',
    freq     VARCHAR(10)  COMMENT '频率',
    speed    VARCHAR(10)  COMMENT '转速',
    status   TINYINT      COMMENT '运行状态(0=停止/1=运行/2=故障)',
    angle    DECIMAL(5,1) COMMENT '叶片角度(°)',
    PRIMARY KEY (st_id, tm)
);
```
> ⚠️ 电气参数（uab/ubc/uca/ia/ib/ic/p/freq/speed）为 varchar 类型，数值比较前需 CAST 或应用层转换

## 大坝安全监测表

### dsm_dfr_srvrds_srhrds（GNSS 位移）
```sql
CREATE TABLE dsm_dfr_srvrds_srhrds (
    st_id       INT          NOT NULL,
    tm          DATETIME     NOT NULL,
    wgs84_delta_h DECIMAL(6,3) COMMENT '高程变化量(mm)',
    wgs84_delta_x DECIMAL(6,3) COMMENT 'X方向变化量(mm)',
    wgs84_delta_y DECIMAL(6,3) COMMENT 'Y方向变化量(mm)',
    wgs84_total_h DECIMAL(8,3) COMMENT '累计高程变化(mm)',
    wgs84_total_x DECIMAL(8,3) COMMENT '累计X方向变化(mm)',
    wgs84_total_y DECIMAL(8,3) COMMENT '累计Y方向变化(mm)',
    speed_gh    DECIMAL(5,2) COMMENT 'H方向速率(mm/d)',
    speed_gx    DECIMAL(5,2) COMMENT 'X方向速率(mm/d)',
    speed_gy    DECIMAL(5,2) COMMENT 'Y方向速率(mm/d)',
    point_id    VARCHAR(50)  COMMENT '测点ID',
    PRIMARY KEY (st_id, tm)
);
```

### st_percolation_r（渗流）
```sql
CREATE TABLE st_percolation_r (
    st_id       INT          NOT NULL,
    tm          DATETIME     NOT NULL,
    percolation DECIMAL(10,2) COMMENT '渗流量(L/s)',
    stcd        VARCHAR(20)  COMMENT '站码',
    eq_code     VARCHAR(50)  COMMENT '设备编码',
    PRIMARY KEY (st_id, tm)
);
```

### st_pressure_r（渗压）
```sql
CREATE TABLE st_pressure_r (
    st_id          INT          NOT NULL,
    tm             DATETIME     NOT NULL,
    ext_pressure   DECIMAL(10,2) COMMENT '渗压(kPa)',
    water_pressure DECIMAL(10,2) COMMENT '水位压力(kPa)',
    ext_temperature DECIMAL(5,1) COMMENT '温度(℃)',
    section_id     INT          COMMENT '断面ID',
    point_id       VARCHAR(50)  COMMENT '测点ID',
    PRIMARY KEY (st_id, tm)
);
```

## 其他监测表

### wq_pcp_d（水质）
```sql
CREATE TABLE wq_pcp_d (
    st_id  INT          NOT NULL,
    tm     DATETIME     NOT NULL,
    ph     DECIMAL(3,1) COMMENT 'pH值',
    do     DECIMAL(5,1) COMMENT '溶解氧(mg/L)',
    nh3n   DECIMAL(6,3) COMMENT '氨氮(mg/L)',
    tn     DECIMAL(6,3) COMMENT '总氮(mg/L)',
    tp     DECIMAL(6,3) COMMENT '总磷(mg/L)',
    PRIMARY KEY (st_id, tm)
);
```

### st_soil_moisture_r（墒情）
```sql
CREATE TABLE st_soil_moisture_r (
    st_id             INT          NOT NULL,
    tm                DATETIME     NOT NULL COMMENT '采集时间',
    soil_water10cm    DECIMAL(5,1) COMMENT '10cm含水量(%)',
    soil_water20cm    DECIMAL(5,1) COMMENT '20cm含水量(%)',
    soil_water30cm    DECIMAL(5,1) COMMENT '30cm含水量(%)',
    soil_water60cm    DECIMAL(5,1) COMMENT '60cm含水量(%)',
    soil_water100cm   DECIMAL(5,1) COMMENT '100cm含水量(%)',
    soil_temp10cm     DECIMAL(4,1) COMMENT '10cm温度(℃)',
    soil_temp20cm     DECIMAL(4,1) COMMENT '20cm温度(℃)',
    soil_temp30cm     DECIMAL(4,1) COMMENT '30cm温度(℃)',
    soil_temp60cm     DECIMAL(4,1) COMMENT '60cm温度(℃)',
    soil_temp100cm    DECIMAL(4,1) COMMENT '100cm温度(℃)',
    ec                DECIMAL(8,2) COMMENT '电导率(uS/cm)',
    ph                DECIMAL(3,1) COMMENT 'pH值',
    tension           DECIMAL(6,2) COMMENT '张力(kPa)',
    groundwater_depth DECIMAL(6,2) COMMENT '地下水位(m)',
    soil_moist_evaluation VARCHAR(10) COMMENT '评价(正常/轻度干旱/中度干旱/严重干旱)',
    PRIMARY KEY (st_id, tm)
);
```

### st_termite_monitor_r（白蚁）
```sql
CREATE TABLE st_termite_monitor_r (
    st_id        INT          NOT NULL,
    tm           DATETIME     NOT NULL COMMENT '采集时间',
    termite_species VARCHAR(50) COMMENT '蚁种',
    pest_density     TINYINT    COMMENT '密度等级(0-4)',
    damage_level     TINYINT    COMMENT '危害等级',
    check_result     VARCHAR(20) COMMENT '检查结果(无白蚁/发现/疑似痕迹)',
    PRIMARY KEY (st_id, tm)
);
```

## 基础信息表

### att_st_base（测站基本表）
```sql
CREATE TABLE att_st_base (
    st_id     INT          PRIMARY KEY,
    st_name   VARCHAR(100) COMMENT '测站名称',
    st_code   VARCHAR(20)  COMMENT '站码',
    st_type   VARCHAR(20)  COMMENT '测站类型(RSVR/RIVER/PPTN/PRESSURE/...)',
    lgtd      DECIMAL(10,6) COMMENT '经度',
    lttd      DECIMAL(10,6) COMMENT '纬度',
    stlc      VARCHAR(200) COMMENT '测站地址',
    status    TINYINT      COMMENT '状态(0=离线/1=在线/2=异常)',
    dam_id    INT          COMMENT '关联大坝ID'
);
```

### eq_equip_base（设备台账）
```sql
CREATE TABLE eq_equip_base (
    id           INT          PRIMARY KEY,
    name         VARCHAR(100) COMMENT '设备名称',
    code         VARCHAR(50)  COMMENT '设备编码',
    type_flag    VARCHAR(50)  COMMENT '设备类型字典',
    status       TINYINT      COMMENT '状态(0=离线/1=在线/2=异常)',
    st_base_id   INT          COMMENT '关联测站',
    project_id   INT          COMMENT '所属项目',
    install_date DATE         COMMENT '安装日期'
);
```

### ew_info_rules（预警规则/阈值）
```sql
CREATE TABLE ew_info_rules (
    id       INT          PRIMARY KEY,
    name     VARCHAR(100) COMMENT '规则名',
    ew_type  CHAR(2)      COMMENT '预警类型(0=水位/1=水质/2=雨量/3=开关变化/4=开关)',
    level_r  VARCHAR(10)  COMMENT '预警级别(I/II/III/IV)',
    st_id    INT          COMMENT '测站ID（空=全局）',
    extend   JSON         COMMENT '扩展配置(阈值JSON)',
    status   TINYINT      COMMENT '状态',
    rule_content TEXT     COMMENT '规则描述'
);
```
`extend` 字段 JSON 示例:
```json
{
  "threshold": 248.0,
  "rate": {"max_change": 0.5, "window": 1},
  "trend": {"consecutive": 6, "window_hours": 6}
}
```

### ew_info_message（预警消息）
```sql
CREATE TABLE ew_info_message (
    id         INT          PRIMARY KEY,
    ew_name    VARCHAR(100) COMMENT '预警名',
    ew_type    VARCHAR(50)  COMMENT '预警类型',
    level_r    VARCHAR(10)  COMMENT '预警级别(I/II/III)',
    value      DECIMAL(10,2) COMMENT '触发值',
    content    TEXT         COMMENT '告警内容',
    st_id      INT          COMMENT '关联测站',
    st_name    VARCHAR(100) COMMENT '测站名称',
    gather_time DATETIME    COMMENT '采集时间',
    status     TINYINT      COMMENT '确认状态(0=未确认/1=已确认)',
    create_time DATETIME    COMMENT '生成时间',
    confirm_time DATETIME   COMMENT '确认时间',
    deleted    TINYINT      DEFAULT 0
);
```

### sys_data_source_registry（数据源注册表）
```sql
CREATE TABLE sys_data_source_registry (
    id             INT          PRIMARY KEY,
    name           VARCHAR(100) COMMENT '数据源名称',
    source_table   VARCHAR(100) COMMENT '源表名',
    keywords       VARCHAR(500) COMMENT '匹配关键词(逗号分隔)',
    station_type   VARCHAR(20)  COMMENT '关联测站类型',
    max_distance   INT          COMMENT '最大匹配距离(m)',
    query_fields   VARCHAR(500) COMMENT '查询字段列表',
    time_field     VARCHAR(50)  COMMENT '时间字段名',
    default_hours  INT          COMMENT '默认查询小时数',
    judge_rules    JSON         COMMENT '判定规则',
    sort_order     INT          COMMENT '排序号',
    status         TINYINT      COMMENT '状态',
    deleted        TINYINT      DEFAULT 0
);
```

## 巡检业务表

### business_check_task（巡检任务）
```sql
CREATE TABLE business_check_task (
    id         INT          PRIMARY KEY,
    name       VARCHAR(200) COMMENT '任务名称',
    status     VARCHAR(20)  COMMENT '状态(1=待巡检/2=巡检中/3=已完成)',
    plan_time  DATETIME     COMMENT '计划时间',
    begin_time DATETIME     COMMENT '实际开始时间',
    end_time   DATETIME     COMMENT '实际结束时间',
    bad_num    INT          COMMENT '缺陷数',
    deleted    TINYINT      DEFAULT 0
);
```

### business_check_error（缺陷记录）
```sql
CREATE TABLE business_check_error (
    id          INT          PRIMARY KEY,
    problem     TEXT         COMMENT '问题描述',
    status      VARCHAR(20)  COMMENT '处理状态',
    deal_time   DATETIME     COMMENT '处理时间',
    create_time DATETIME     COMMENT '创建时间',
    deleted     TINYINT      DEFAULT 0
);
```

## 常见 SQL 查询模式

### 水库查询
```sql
-- 最近一周水位变化
SELECT tm, rz, inq, otq FROM st_rsvr_r WHERE st_id = ? AND tm > DATE_SUB(NOW(), INTERVAL 7 DAY) ORDER BY tm;
-- 最新数据
SELECT * FROM st_rsvr_r WHERE st_id = ? ORDER BY tm DESC LIMIT 1;
```

### 河道查询
```sql
SELECT tm, z, q FROM st_river_r WHERE st_id = ? AND tm > DATE_SUB(NOW(), INTERVAL 7 DAY);
```

### 雨量查询
```sql
-- 今日降雨量
SELECT st_id, SUM(p) as total FROM st_pptn_r WHERE DATE(tm) = CURDATE() GROUP BY st_id;
-- 日雨量历史
SELECT dt, dp FROM st_pptn_dp_s WHERE st_id = ? AND dt > DATE_SUB(NOW(), INTERVAL 30 DAY);
```

### 设备查询
```sql
-- 离线设备
SELECT name, code FROM eq_equip_base WHERE status = 0 AND deleted = 0;
-- 异常记录
SELECT * FROM eq_data_anomaly_record WHERE equipment_code = ?;
```

### 预警查询
```sql
-- 最近预警
SELECT ew_name, level_r, value, gather_time FROM ew_info_message WHERE deleted = 0 ORDER BY gather_time DESC LIMIT 20;
-- II级以上预警
SELECT * FROM ew_info_message WHERE level_r IN ('1','2') AND gather_time > DATE_SUB(NOW(), INTERVAL 7 DAY);
```

### 巡检查询
```sql
-- 未完成任务
SELECT name, plan_time, status FROM business_check_task WHERE status != 'completed' AND deleted = 0;
-- 本月缺陷
SELECT problem, create_time FROM business_check_error WHERE MONTH(create_time) = MONTH(NOW());
```

### 聚合查询
```sql
-- 按月统计平均水位
SELECT DATE_FORMAT(tm, '%Y-%m') as month, AVG(rz) FROM st_rsvr_r WHERE deleted = 0 GROUP BY month;
```

## 注意事项

- 所有查询需带 `AND deleted = 0` 软删除过滤（业务表）
- 多租户环境需带 `AND tenant_id = ?` 过滤
- 时间字段通用格式: `tm` (datetime)
- 大数据量查询限制: max-num = 2000
- 默认显示行数: display-num = 20
- 泵站电气参数（rei_pump_r.ia/ib/ic等）为 varchar 类型，数值比较前需 CAST 或应用层转换
- 雨量时段长：`st_pptn_r.dr` 单位**分钟**，`st_pptn_region_r.intv` 单位**小时**
