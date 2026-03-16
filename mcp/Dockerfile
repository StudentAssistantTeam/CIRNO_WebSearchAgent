#构建python server
FROM docker.1ms.run/python:3.13

COPY ["./requirements.txt", "./"]
# 调试：检查文件是否存在
RUN ls -la && cat requirements.txt
# 安装uv
RUN pip install uv -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple

COPY . .

# 给 entrypoint.sh 添加执行权限
RUN chmod +x /entrypoint.sh

EXPOSE 50055
ENTRYPOINT ["./entrypoint.sh"]