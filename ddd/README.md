# 忘れそうなコマンド残しておく

- protoファイルから、Pythonのコード作成するやつ
```
cd ddd

poetry run python -m grpc_tools.protoc \           
  -I ./src/proto \     
  --python_out=./src/pb \
  --pyi_out=./src/pb \      
  --grpc_python_out=./src/pb \
  ./src/proto/todo.proto
```

- grpcの立ち上げ
```
cd ddd

PYTHONPATH=src poetry run python src/ddd/infrastructure/grpc/todo_grpc_server.py
```