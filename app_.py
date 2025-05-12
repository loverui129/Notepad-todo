# 导入 Flask 框架
from flask import Flask, request, jsonify

# 创建一个 Flask 应用实例
app = Flask(__name__)

# 设置路由，指定只接受 POST 请求
@app.route('/predict', methods=['POST'])
def predict():
    # 从请求中解析出 JSON 数据
    data = request.get_json()

    # 获取 "features" 字段，如果不存在则默认为空列表
    features = data.get('features', [])

    # 检查 features 是否是由数字构成的列表
    if not isinstance(features, list) or not all(isinstance(x, (int, float)) for x in features):
        return jsonify({'error': 'Invalid input format'}), 400

    # 简单的预测逻辑：求和
    prediction = sum(features)

    # 返回结果，类型为 JSON
    return jsonify({'prediction': prediction})

# 启动服务（如果直接运行这个文件）
if __name__ == '__main__':
    app.run(debug=True)

