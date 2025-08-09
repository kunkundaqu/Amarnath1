# 🚀 AI Trading Platform - 部署配置指南

## 🔧 必需的环境变量

在Render.com部署时，您需要配置以下环境变量：

### 📊 Supabase 数据库配置
```
SUPABASE_URL=https://poqloztmhyznarxrpllr.supabase.co
SUPABASE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InBvcWxvenRtaHl6bmFyeHJwbGxyIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMzNzk3MDYsImV4cCI6MjA2ODk1NTcwNn0.Idy9FOtkKLw_joudPSn_aE3OMz5Zl4e76FeJ_0Ww_UM
```

### 🎯 交易员配置
```
Web_Trader_UUID=b276f479-0910-418f-adc7-8762be79435f
```

### 🤖 OpenAI API配置（AI功能必需）
```
OPENAI_API_KEY=sk-proj-your-openai-api-key-here
```
**注意：请使用您之前提供的实际OpenAI API密钥**

### 🔐 Flask安全配置
```
FLASK_SECRET_KEY=your_secure_random_secret_key_change_this
```

## 🎯 Render.com 部署步骤

### 1. 进入Render Dashboard
- 登录 [render.com](https://render.com)
- 选择您的Web Service

### 2. 配置环境变量
- 点击 "Environment" 选项卡
- 点击 "Add Environment Variable"
- 逐个添加上述所有环境变量

### 3. 重新部署
- 点击 "Manual Deploy" 
- 或等待自动部署触发

## ⚠️ 常见部署问题排查

### VIP 和 Likes 显示 "Error"
**可能原因：**
1. `SUPABASE_URL` 或 `SUPABASE_KEY` 配置错误
2. `Web_Trader_UUID` 不匹配数据库中的数据
3. Supabase数据库表结构缺失

**解决方案：**
1. 确认所有环境变量正确配置
2. 检查Supabase数据库连接状态
3. 确认 `trader_profiles` 表存在且包含正确的 `trader_uuid`

### AI功能不工作
**可能原因：**
1. `OPENAI_API_KEY` 未配置或无效
2. OpenAI API余额不足

**解决方案：**
1. 验证API密钥有效性
2. 检查OpenAI账户余额

## 📝 部署验证清单

- [ ] 所有环境变量已配置
- [ ] Supabase数据库连接正常
- [ ] OpenAI API密钥有效
- [ ] 应用成功启动（无ModuleNotFoundError）
- [ ] 主页可以正常访问
- [ ] VIP功能正常（不显示Error）
- [ ] AI工具可以访问
- [ ] 弹窗系统工作正常

## 🎉 成功部署标志

当所有配置正确后，您应该看到：
- ✅ 主页正常加载
- ✅ VIP区域显示正确数据（不是Error）
- ✅ AI工具页面可访问
- ✅ 管理后台功能正常
- ✅ 弹窗系统按预期工作
