class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_map = {}
        for c in t:
            t_map[c] = t_map.get(c, 0) + 1
        need = len(t_map)

        window = {}
        min_len = float("inf")
        have = 0
        left = 0

        for right in range(len(s)):
            current = s[right]

            if current in t_map:
                window[current]=window.get(current, 0) + 1

                if window[current] == t_map[current]:
                    have += 1

            while have == need:
                window_len = right - left + 1
                if window_len < min_len:
                    start = left
                    end = right
                    min_len = min(window_len, min_len)

                left_char = s[left]
                if left_char in t_map:
                    window[left_char] -= 1
                    if window[left_char] < t_map[left_char]:
                        have -= 1

                left += 1
        
        if min_len==float("inf"):
            return ""
        return s[start:end+1]
