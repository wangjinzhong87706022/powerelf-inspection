# ⚠️ 本仓库已归档（Archived）

> **此仓库已停止维护，内容已迁入统一 monorepo。**
>
> 🔗 新仓库：**[wangjinzhong87706022/powerelf-skills](https://github.com/wangjinzhong87706022/powerelf-skills)**
>
> 本 skill 在新仓库中的位置：`powerelf-skills/powerelf-inspection/`
>
> **请勿在此提交或推送** —— 所有后续开发在新 monorepo 进行。

---

## 迁移说明（2026-07-10）

- 原 4 个独立 skill 仓库（data-governance / early-warning / inspection / chatbi）+ 未版本化的 monitor 已整合为单一 monorepo [`powerelf-skills`](https://github.com/wangjinzhong87706022/powerelf-skills)。
- 新增 `_shared/` 跨 skill 共享层：统一数据库连接（`lib/db.py`，`POWERELF_DB_*` + `SRM_DB_*` 后备）、`bootstrap.sh`（导出 `DB_URL`）、唯一表结构源（`references/schema.md`）、共享算法/规则、REST 鉴权约定。
- 各 skill 通过相对路径引用 `_shared/`，必须**整体 clone monorepo** 使用，不可单独取用本仓库。
- 安全：全部硬编码 DB 密码已清除，统一走环境变量。

**如需继续使用本 skill，请到 [powerelf-skills](https://github.com/wangjinzhong87706022/powerelf-skills) 获取最新版本。**
