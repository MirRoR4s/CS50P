
- args 是位置参数，类似于 `print("Hello", "World")` 
- kargs 是命名参数（或者称关键字参数），类似于 `print("Hello", "World")`

在定义函数时，可以声明我们的函数期望接收任意数量的位置参数和命名参数，示例如下：

```python
def f(*args, **kwargs):
    print("Positional:", args)


f(100, 50, 25)
```

观察一下 print 函数的原型：
```python
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
```
`*objects` 表明接收任意数量的位置参数。