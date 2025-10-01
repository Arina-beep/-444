import heapq
from collections import Counter


class HuffmanNode:
    """Узел дерева Хаффмана"""

    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


class HuffmanTree:
    """Дерево Хаффмана"""

    def __init__(self, text):
        if not text or not isinstance(text, str):
            raise ValueError("Входные данные должны быть непустой строкой")

        if len(text) < 2:
            raise ValueError("Текст должен содержать хотя бы 2 символа")

        self.text = text
        self.codes = {}
        self.root = self._build_tree()
        self._generate_codes(self.root, "")

    def _build_tree(self):
        """Построение дерева Хаффмана"""
        freq = Counter(self.text)

        heap = []
        for char, count in freq.items():
            heapq.heappush(heap, HuffmanNode(char, count))

        while len(heap) > 1:
            left = heapq.heappop(heap)
            right = heapq.heappop(heap)

            merged = HuffmanNode(None, left.freq + right.freq)
            merged.left = left
            merged.right = right

            heapq.heappush(heap, merged)

        return heap[0] if heap else None

    def _generate_codes(self, node, current_code):
        """Генерация кодов для символов"""
        if node is None:
            return

        if node.char is not None:
            self.codes[node.char] = current_code if current_code else "0"
            return

        self._generate_codes(node.left, current_code + "0")
        self._generate_codes(node.right, current_code + "1")

    def print_codes(self):
        """Вывод кодов для всех символов"""
        print("Коды Хаффмана:")
        sorted_codes = sorted(self.codes.items(), key=lambda x: (len(x[1]), x[1]))

        for char, code in sorted_codes:
            if char == ' ':
                display_char = '[ПРОБЕЛ]'
            elif char == '\n':
                display_char = '[ПЕРЕНОС]'
            elif char == '\t':
                display_char = '[ТАБУЛЯЦИЯ]'
            else:
                display_char = char
            print(f"'{display_char}': {code}")

    def print_tree(self, node=None, level=0, prefix="", is_last=True):
        """Вывод структуры дерева"""
        if node is None:
            node = self.root
            print("Структура дерева:")

        connector = "└── " if is_last else "├── "
        indent = "    " * level

        if node.char is not None:
            if node.char == ' ':
                char_display = '[ПРОБЕЛ]'
            elif node.char == '\n':
                char_display = '[ПЕРЕНОС]'
            elif node.char == '\t':
                char_display = '[ТАБУЛЯЦИЯ]'
            else:
                char_display = node.char
            print(f"{indent}{connector}'{char_display}': {node.freq}")
        else:
            print(f"{indent}{connector}● (freq: {node.freq})")

        children = []
        if node.left:
            children.append(node.left)
        if node.right:
            children.append(node.right)

        for i, child in enumerate(children):
            is_last_child = (i == len(children) - 1)
            self.print_tree(child, level + 1, "", is_last_child)


def main():
    """Главная функция программы"""
    try:
        text = input("Введите фразу для кодирования: ").strip()

        if not text:
            print("Ошибка: текст не может быть пустым")
            return

        if len(text) < 2:
            print("Ошибка: текст должен содержать хотя бы 2 символа")
            return

        huffman = HuffmanTree(text)

        print()
        huffman.print_codes()

        print()
        huffman.print_tree()

    except Exception as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()