class Todo:
    def __init__(self, title):
        self.title = title
        self.is_complete = False

    def edit(self, new_title):
        self.title = new_title

    def toggle_complete(self):
        self.is_complete = not self.is_complete  # True > False로, F > T로

    def __str__(self):
        status = "v" if self.is_complete else " "
        return f"[{status}] {self.title}"


## 관리하는 역할
class TodoManager:
    def __init__(self):
        self.todos = []

    # 생성
    def create_todo(self, title):
        todo = Todo(title)
        self.todos.append(todo)

    # 삭제/ 인덱스값 활용해서 n번째걸 지워줘
    # idx: 1 ~ len(todos)
    def remove_todo(self, idx):
        del self.todos[idx - 1]
        # if 1 <= index <= len(self.todos + 1):
        #     removed = self.todos.pop(index)
        #     print(f"{index}번이 삭제되었습니다.")

    # 타이틀 수정
    # idx, title
    def edit_todo(self, idx, title):
        # self.todos[idx - 1].title = title
        self.todos[idx - 1].edit(title)

    # 완료여부 수정
    # idx
    def check_todo(self, idx):
        self.todos[idx - 1].toggle_complete()

    # 조회
    def search_todos(self):
        for i, t in enumerate(self.todos):
            print(f"{i + 1}.{t}")
        # for i in Todo:
        #     if i.find():
        #         return

    # 저장 (14_파일입출력 참고)
    def save_to_file(self):
        with open("todo_list.txt", "w", encoding="utf-8") as f:
            for t in self.todos:
                f.write(f"{t.title}/{"T" if t.is_complete else "F"}")
                # 할일명/T
                # 할일명/F
                # [v] 할 일

    # 불러오기
    def load_by_file(self):
        try:
            with open("todo_list.txt", "r", encoding="utf-8") as f:
                for line in f:
                    # line: 할일/T
                    data = line.split("/")
                    todo = Todo(data[0])
                    todo.is_complete = data[1] == "T"
                    self.todos.append(todo)
        except:
            pass


def menu():
    manager = TodoManager()
    manager.load_by_file()

    while True:
        print("=" * 20)
        prompt = """
        1. 조회
        2. 생성
        3. 삭제
        4. 타이틀 수정
        5. 할 일 체크
        0. 종료 및 저장
        """
        print(prompt)
        print("=" * 20)
        user = input("입력: ")
        if user == "1":
            manager.search_todos()
        elif user == "2":
            title = input("할 일 입력:")
            manager.create_todo(title)
        elif user == "3":
            manager.search_todos()
            idx = input("지울 번호 입력: ")
            manager.remove_todo(int(idx))
        elif user == "4":  # 인덱스값 받고나서
            manager.search_todos()
            idx = input("수정할 번호 입력: ")
            new_title = input("새로운 제목 입력: ")
            manager.edit_todo(int(idx), new_title)
        elif user == "5":
            manager.search_todos()
            idx = input("체크할 번호 입력: ")
            manager.check_todo(int(idx))
        elif user == "0":
            manager.save_to_file()
            break


if __name__ == "__main__":
    menu()
