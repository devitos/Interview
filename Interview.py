class Stack:
    inv = {'(': ')', '[': ']', '{': '}', '<': '>'}

    def __init__(self, elements=None):
        if elements == None:
            self.st = list()
        else:
            self.st = list()
            elem_list = list(elements)
            for elem in elem_list:
                self.st.append(elem)

    def __str__(self):
        string = str(self.st)
        return string

    def isEmpty(self):
        if self.st == []:
            result = True
        else:
            result = False
        return result

    def push(self, elem: str):
        if elem not in self.inv:
            print(f'Недопустисый элемент => {elem}')

        elif self.isEmpty() == True:
            self.st.append(elem)
            self.st.append(self.inv[elem])
        else:
            m = len(self.st) // 2
            self.st.insert(m, self.inv[elem])
            self.st.insert(m, elem)
        return

    def pop(self):
        if self.isEmpty() == False:
            m = len(self.st) // 2
            result = list()
            result.append(self.st.pop(m-1))
            result.append(self.st.pop(m-1))
        else:
            result = 0
        return result

    def peek(self):
        if self.isEmpty() == False:
            result = list()
            m = len(self.st) // 2
            result.append(self.st[m-1])
            result.append(self.st[m])
        else:
            result = None
        return result

    def size(self):
        result = len(self.st)
        return result

    def isBalance(self):
        a = self.st
        if self.isEmpty() == False and len(self.st) % 2 == 0:
            a = self.peek()
            while a[0] in self.inv.keys() and a[1] == self.inv[a[0]]:
                self.pop()
                a = self.peek()
                if self.st == []:
                    result1 = 'Сбаланасирован по циклу'
                    break
            else:
                for elems in self.st:
                    if elems not in self.inv.keys() and elems not in self.inv.values():
                        result1 = f'НЕСБАЛАНСИРОВАН, ЭЛЕМЕНТ {elems} не входит в список допустимых элементов'
                        break
                    elif elems not in self.inv:
                        continue
                    elif (self.st.index(elems) - self.st.index(self.inv[elems])) % 2 == 1 and \
                            self.st.count(elems) == self.st.count(self.inv[elems]) and \
                            (self.st.index(self.inv[elems]) - self.st.index(elems)) >= 0:
                        result1 = 'Сбаланасирован по методу'

                    else:
                        result1 = f'НЕСБАЛАНСИРОВАН из-за {elems}'
                        # print(self.st.index(elems))
                        # print(self.st.index(self.inv[elems]))
                        # print((self.st.index(elems) - self.st.index(self.inv[elems])) % 2)
                        break
        else:
            result1 = 'СПИСОК ПУСТ ИЛИ НЕЧЕТНОЕ КОЛИЧЕСТВО ЭЛЕМНТОВ'
        self.st = a
        return print(result1)


if __name__ == '__main__':
    new_stack = Stack('(((([{}]))))')
    new_stack.isEmpty()
    new_stack.push('(')
    new_stack.push('{')
    new_stack.push('<')
    new_stack.push('<')
    new_stack.push('s')
    new_stack.pop()
    new_stack.pop()
    new_stack.peek()
    print(new_stack)
    print(new_stack.size())
    new_stack.isBalance()


#  вот такой стэк не удаётся проверить на баланс <<<[([]()()(([[[]]])))]{()}>>>