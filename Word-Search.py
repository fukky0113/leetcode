class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        h = len(board)
        w = len(board[0])
        word_l = len(word)

        if h == 1 and w == 1:
            return board[0][0] == word
            
        def explore_word(pos, index):
            if index == word_l:
                return True
                            
            y, x = pos
            if board[y][x] != word[index]:
                return False

            char = board[y][x]
            board[y][x] = '#'
            for off_y, off_x in [(-1,0), (1,0), (0,1), (0,-1)]:
                if 0 <= y+off_y < h and 0 <= x+off_x < w:
                    if explore_word((y+off_y, x+off_x), index+1):
                        return True
            board[y][x] = char
            return False

        for y in range(h):
            for x in range(w):
                if explore_word((y, x), 0):
                    return True
        return False
