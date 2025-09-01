# 专业交易平台 (Professional Trading Platform)

这是一个基于Flask的专业交易平台，提供实时股票交易数据、用户管理和VIP会员系统。

## 功能特性

### 核心功能
- **实时股票价格查询**: 支持美国和印度股票市场的实时价格获取
- **交易记录管理**: 完整的交易历史记录和持仓管理
- **用户认证系统**: 安全的用户登录和权限管理
- **VIP会员系统**: 多级会员体系，不同等级享受不同权益
- **排行榜系统**: 交易员收益排行榜
- **WhatsApp客服**: 智能客服分配系统

### 管理功能
- **管理员后台**: 完整的后台管理系统
- **用户管理**: 用户创建、编辑、权限分配
- **交易员管理**: 交易员资料管理
- **公告系统**: 弹窗公告和系统通知
- **策略管理**: 交易策略发布和管理

## 技术栈

- **后端**: Flask (Python)
- **数据库**: Supabase (PostgreSQL)
- **股票数据**: yfinance, Polygon.io API
- **实时价格**: 自定义API集成
- **前端**: HTML, CSS, JavaScript
- **部署**: Render, Heroku

## 安装和运行

### 环境要求
- Python 3.8+
- pip

### 安装步骤

1. 克隆仓库
```bash
git clone https://github.com/kunkundaqu/Amarnath1.git
cd Amarnath1
```

2. 安装依赖
```bash
pip install -r requirements.txt
```

3. 配置环境变量
创建 `.env` 文件并添加以下配置：
```env
FLASK_SECRET_KEY=your_secret_key_here
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key
Web_Trader_UUID=your_trader_uuid
OPENAI_API_KEY=your_openai_api_key
```

4. 运行应用
```bash
python app.py
```

应用将在 `http://localhost:5000` 启动

## 项目结构

```
Web-new-8-29/
├── app.py                 # 主应用文件
├── supabase_client.py     # Supabase客户端配置
├── requirements.txt       # Python依赖
├── templates/            # HTML模板
│   ├── index.html        # 首页
│   ├── vip.html          # VIP页面
│   ├── admin/            # 管理后台模板
│   └── ...
├── static/               # 静态资源
│   ├── styles.css        # 样式文件
│   └── badges/           # 徽章图片
├── backend/              # 后端模块
│   └── trading/          # 交易相关功能
└── frontend/             # 前端模块
    └── templates/        # 前端模板
```

## API接口

### 用户认证
- `POST /api/login` - 用户登录
- `POST /api/logout` - 用户登出
- `GET /api/check-login` - 检查登录状态

### 交易数据
- `GET /api/price` - 获取实时价格
- `GET /api/history` - 获取历史数据
- `GET /api/best-trade-info` - 获取最佳交易信息

### 管理接口
- `GET /api/admin/users` - 获取用户列表
- `POST /api/admin/users` - 创建用户
- `PUT /api/admin/users/<id>` - 更新用户
- `DELETE /api/admin/users/<id>` - 删除用户

### 公告系统
- `GET /api/announcement` - 获取公告
- `POST /api/admin/announcement` - 创建公告
- `PUT /api/admin/announcement/<id>` - 更新公告
- `DELETE /api/admin/announcement/<id>` - 删除公告

## 数据库表结构

### 主要表
- `users` - 用户表
- `trades1` - 交易记录表
- `trader_profiles` - 交易员资料表
- `announcements` - 公告表
- `membership_levels` - 会员等级表
- `vip_trades` - VIP交易记录表

## 部署

### Render部署
项目包含 `render.yaml` 配置文件，可以直接部署到Render平台。

### 环境变量配置
确保在生产环境中正确配置所有必需的环境变量。

## 定时任务

应用包含以下定时任务：
- 每30秒更新持仓股票价格
- 每30秒更新印度股票价格
- 每30秒同步所有交易表的实时价格

## 安全特性

- 用户认证和授权
- 密码加密存储
- API访问控制
- 设备指纹识别
- 登录日志记录

## 贡献

欢迎提交Issue和Pull Request来改进这个项目。

## 许可证

本项目采用MIT许可证。

## 联系方式

如有问题，请通过GitHub Issues联系。
