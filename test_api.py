#!/usr/bin/env python3
"""
API测试脚本 - 用于验证VIP和Likes API是否正常工作
"""

import requests
import json
import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

def test_trader_api():
    """测试交易员API"""
    print("🔍 测试交易员API...")
    
    # 获取基础URL
    base_url = os.getenv('BASE_URL', 'http://localhost:5000')
    if not base_url.startswith('http'):
        base_url = f'http://{base_url}'
    
    try:
        # 测试 /api/trader 端点
        response = requests.get(f'{base_url}/api/trader', timeout=10)
        print(f"状态码: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"响应数据: {json.dumps(data, indent=2, ensure_ascii=False)}")
            
            if data.get('success'):
                trader = data.get('trader', {})
                print(f"✅ API正常工作")
                print(f"   - 交易员名称: {trader.get('trader_name', 'N/A')}")
                print(f"   - 会员数量: {trader.get('members_count', 'N/A')}")
                print(f"   - 点赞数量: {trader.get('likes_count', 'N/A')}")
                return True
            else:
                print(f"❌ API返回错误: {data.get('message', 'Unknown error')}")
                return False
        else:
            print(f"❌ HTTP错误: {response.status_code}")
            print(f"响应内容: {response.text}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"❌ 请求失败: {e}")
        return False
    except json.JSONDecodeError as e:
        print(f"❌ JSON解析失败: {e}")
        print(f"响应内容: {response.text}")
        return False

def test_like_api():
    """测试点赞API"""
    print("\n🔍 测试点赞API...")
    
    base_url = os.getenv('BASE_URL', 'http://localhost:5000')
    if not base_url.startswith('http'):
        base_url = f'http://{base_url}'
    
    try:
        # 测试点赞功能
        data = {'id': '0'}
        response = requests.post(
            f'{base_url}/api/like-trader',
            json=data,
            headers={'Content-Type': 'application/json'},
            timeout=10
        )
        
        print(f"状态码: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"响应数据: {json.dumps(data, indent=2, ensure_ascii=False)}")
            
            if data.get('success'):
                print(f"✅ 点赞API正常工作")
                print(f"   - 当前点赞数: {data.get('likes_count', 'N/A')}")
                return True
            else:
                print(f"❌ 点赞API返回错误: {data.get('message', 'Unknown error')}")
                return False
        else:
            print(f"❌ HTTP错误: {response.status_code}")
            print(f"响应内容: {response.text}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"❌ 请求失败: {e}")
        return False
    except json.JSONDecodeError as e:
        print(f"❌ JSON解析失败: {e}")
        print(f"响应内容: {response.text}")
        return False

def check_environment():
    """检查环境变量"""
    print("🔍 检查环境变量...")
    
    required_vars = [
        'SUPABASE_URL',
        'SUPABASE_KEY',
        'Web_Trader_UUID'
    ]
    
    missing_vars = []
    for var in required_vars:
        value = os.getenv(var)
        if value:
            print(f"✅ {var}: {'*' * len(value)} (已设置)")
        else:
            print(f"❌ {var}: 未设置")
            missing_vars.append(var)
    
    if missing_vars:
        print(f"\n⚠️  缺少环境变量: {', '.join(missing_vars)}")
        print("请确保在.env文件中设置了这些变量")
        return False
    else:
        print("✅ 所有必需的环境变量都已设置")
        return True

def main():
    """主函数"""
    print("🚀 开始API测试...\n")
    
    # 检查环境变量
    env_ok = check_environment()
    if not env_ok:
        print("\n❌ 环境变量配置不完整，请先配置.env文件")
        return
    
    print("\n" + "="*50)
    
    # 测试交易员API
    trader_ok = test_trader_api()
    
    print("\n" + "="*50)
    
    # 测试点赞API
    like_ok = test_like_api()
    
    print("\n" + "="*50)
    
    # 总结
    print("📊 测试总结:")
    if trader_ok and like_ok:
        print("✅ 所有API测试通过！VIP和Likes功能应该正常工作")
    else:
        print("❌ 部分API测试失败，请检查以下问题:")
        if not trader_ok:
            print("   - 交易员API (/api/trader) 可能有问题")
        if not like_ok:
            print("   - 点赞API (/api/like-trader) 可能有问题")
        print("\n💡 建议:")
        print("   1. 检查Supabase数据库连接")
        print("   2. 确认trader_profiles表存在且有数据")
        print("   3. 检查Web_Trader_UUID是否正确")
        print("   4. 查看应用日志获取详细错误信息")

if __name__ == "__main__":
    main()
