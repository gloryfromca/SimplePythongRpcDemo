# Simple Python gRpc Demo      

### Build

#### generate target code
``` bin     
protoc -I. -I/usr/local/include --python_out=../src --grpc_python_out=../src --plugin=protoc-gen-grpc_python=/home/zh/grpc/bins/opt/grpc_python_plugin ComputeService.proto
```

`-I` options should include src code file and imported packages. for instance, `.` includes src code file: ComputeService.proto and `google/api/..` which are packages copied into this project, 
`/usr/local/include` includes `google/protobuf/..` which are installed when installing `protoc`.      

`python_out` option is path of result that protobuffer definition is translated to python.        

`grpc_python_out` option is path that gRpc client and service python code of related protobuffer definition.     

`--plugin` option is plugin for extended function. `protoc-gen-grpc_python=/home/zh/grpc/bins/opt/grpc_python_plugin` is plugin for
generating gRpc code of python version.     

`ComputeService.proto` is protobuffer code file which defines `message` and `service`.    

#### build official proto file    
``` bin    
protoc -I. -I/usr/local/include --python_out=../src  google/api/annotations.proto
```    
`google/api` in `src` don't be used in demo code.

### Installation    
`grpcio-tools`     
```bin
python -m pip install grpcio
python -m pip install grpcio-tools
python -m grpc_tools.protoc --version
```    
compile using grpc tools as a python module.    
`python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. helloworld.proto`

OR     

`protoc`     
official repository: `https://github.com/google/protobuf`     

`RPC library and framework`     
official repository: `https://github.com/grpc/grpc.git`     


### Reference      
https://github.com/grpc/grpc/issues/15675      
https://stackoverflow.com/questions/46131022/protocol-buffer-import-resolution/49537333    
https://grpc.io/docs/tutorials/basic/python/    

