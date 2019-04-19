
python在指定行前插入一行

转载 https://blog.csdn.net/wjciayf/article/details/49638735

以下脚本为，把 ./test/test.txt 的"the first line"前插入一行"the second line"

## 插入位置

其中

```
    def _inserted_newline_list(self):
        if self._get_specify_lineno():
            ls = os.linesep
            f = open("%s" % self.__file)
            li = f.readlines()
            f.close()
            li.insert(self._get_specify_lineno() + 0, self.__newline + ls )
            return li
```

中的 `li.insert(self._get_specify_lineno() + 0, self.__newline + ls )` 中的

- `- 1` 表示向上一行插入
- `+ 0` 表示向下一行插入
- `+ 1` 表示向下2行插入

