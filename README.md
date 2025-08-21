# 专业交易平台 (Professional Trading Platform)

这是一个基于Flask和Supabase构建的专业交易平台，提供实时股票价格、交易管理、VIP会员系统等功能。

## 功能特性

### 🚀 核心功能
- **实时股票价格**: 支持美国和印度股票市场的实时价格查询
- **交易管理**: 完整的交易记录管理，包括买入、卖出、持仓等
- **VIP会员系统**: 多级会员体系，提供差异化服务
- **排行榜系统**: 交易员收益排行榜
- **公告系统**: 实时公告和弹窗通知
- **WhatsApp客服**: 智能客服分配系统

### 📊 交易功能
- 多市场支持（美国、印度）
- 实时价格更新（每30秒）
- 历史数据查询
- 盈亏计算和统计
- 交易策略管理

### 👥 用户管理
- 用户注册和登录
- 会员等级管理
- 权限控制
- 个人资料管理

### 🎯 管理功能
- 交易员管理
- 用户管理
- 公告管理
- 策略管理
- 系统监控

## 技术架构

### 后端技术
- **Flask**: Web框架
- **Supabase**: 数据库和认证服务
- **MySQL**: 关系型数据库
- **APScheduler**: 定时任务调度
- **yfinance**: 股票数据API
- **OpenAI**: AI功能集成

### 前端技术
- **HTML5/CSS3**: 现代化UI设计
- **JavaScript**: 交互功能
- **Bootstrap**: 响应式布局
- **Chart.js**: 数据可视化

### 部署配置
- **Gunicorn**: WSGI服务器
- **Procfile**: Heroku部署配置
- **render.yaml**: Render部署配置

## 安装和运行

### 环境要求
- Python 3.8+
- MySQL 8.0+
- Supabase账户

### 安装步骤

1. 克隆项目
```bash
git clone https://github.com/kunkundaqu/Amarnath1.git
cd Amarnath1
```

2. 安装依赖
```bash
pip install -r requirements.txt
```

3. 配置环境变量
创建 `.env` 文件并配置以下变量：
```env
FLASK_SECRET_KEY=your_secret_key
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key
Web_Trader_UUID=your_trader_uuid
OPENAI_API_KEY=your_openai_api_key
```

4. 运行应用
```bash
python app.py
```

### 数据库设置

1. 创建MySQL数据库
```sql
CREATE DATABASE trading_platform;
```

2. 运行SQL脚本
```bash
mysql -u root -p trading_platform < schema.sql
```

## 项目结构

```
Web-New-8-19-1111/
├── app.py                 # 主应用文件
├── supabase_client.py     # Supabase客户端
├── requirements.txt       # Python依赖
├── Procfile             # Heroku部署配置
├── render.yaml          # Render部署配置
├── backend/             # 后端模块
│   └── trading/        # 交易相关功能
├── frontend/            # 前端模板
│   └── templates/      # HTML模板
├── static/              # 静态资源
│   ├── styles.css      # 样式文件
│   └── badges/         # 徽章图片
└── templates/           # 主模板目录
    ├── admin/          # 管理后台模板
    ├── index.html      # 首页
    ├── vip.html        # VIP页面
    └── ...
```

## API接口

### 认证接口
- `POST /api/login` - 用户登录
- `POST /api/logout` - 用户登出
- `GET /api/check-login` - 检查登录状态

### 交易接口
- `GET /api/price` - 获取实时价格
- `GET /api/history` - 获取历史数据
- `GET /api/best-trade-info` - 获取最佳交易信息

### 管理接口
- `GET/POST /api/admin/users` - 用户管理
- `GET/POST /api/admin/trader` - 交易员管理
- `GET/POST /api/admin/announcement` - 公告管理

## 部署

### Heroku部署
```bash
git push heroku main
```

### Render部署
项目包含 `render.yaml` 配置文件，可直接在Render平台部署。

## 贡献

欢迎提交Issue和Pull Request来改进项目。

## 许可证

本项目采用MIT许可证。

## 联系方式

如有问题，请通过GitHub Issues联系。

---

**注意**: 这是一个专业的交易平台，请确保在正式环境中使用前进行充分的测试和安全配置。
