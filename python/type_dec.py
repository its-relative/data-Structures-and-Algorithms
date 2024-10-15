# from typing import List, Dict, Set, Optional, Any


# x : list[list[str]] = [["HI","THIS","IS"]]

# vector = list[float] # storing a type inside a variable

# def foo(v : vector) -> vector:
#     pass

# foo([1.2,3.2])

# def foo(bar:Optional[bool]=False) -> bool:
#     if bar == False:
#         return True
#     else:
#         return bar
    
# foo(False)


# def foo(bar : Any) -> Any:
#     return bar

# print(foo("HI"))


# from typing import Sequence

# def foo(bar : Sequence[int]):

#     return bar

# print(foo([1,2,3,4]))
# # print(foo(["1","2","3","4"]))

# def foo()


# from typing import Callable, Any, Dict

# # x = Callable[[Any, Dict[str, Any]], Any]
# def f(d: Dict[str, str]) -> Dict[str, str]:
#     return {"HI":"There"}

# def foo(func: Callable[[Any, Dict[str, Any]], Any]):
#     pass

# foo(f)