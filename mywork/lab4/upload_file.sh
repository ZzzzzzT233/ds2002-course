#!/bin/bash

aws s3 cp cat.jpg s3://ds2002-mgv8dh
aws s3 presign --expires-in 604800 s3://ds2002-mgv8dh/cat.jpg
#https://ds2002-mgv8dh.s3.us-east-1.amazonaws.com/cat.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIA4MTWH63YKOPYYXUO%2F20240227%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240227T164157Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Security-Token=FwoGZXIvYXdzEAEaDDWNQbdcL3WYByg78SLEAR0GNIM2r68hS9HPvFo%2Fkkf29iU1o2QuysG3N%2FbDk%2BEG%2F0f7sR7kEgdxS1%2BNnHrTZHmFFP2f4t9pFX8TMZn4ZLxwxh%2FfHf%2FVUgxdG71uHnpOhD9369vk7Y1WFKl5eZCOh9nO9aX0fyjhU2k4oaguTFC3aTd6UDeDSisNQ066PIsDB9LapwiHNx98OtEoqsCaQU8UeNCuPpfVKjPH2IE4n8fezxQyc9F34cTXg%2BDJ%2Frgaf8qv8XCXCHhYqHSiD%2FOLYmD0t6IogY34rgYyLW%2BVtJbhnx5lHz5ZwvwWTWv58e9WbOhJqyDQo1V9ctMDSUg9HO%2FbDXCrPd2Wcw%3D%3D&X-Amz-Signature=ae33ffffb31b0417f2b78ddab875e2816eb7849ecf69ca20be5d4b5643d7a98a
