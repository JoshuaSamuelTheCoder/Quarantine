class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        #iterate through list
        #store hashmap of key: str, val: hashmap counter of letters
        # Time: O(n^2), Space: O(n*len(s))

        #iterate through list
        #sort each string, add if permutation
        # Time: O(n^2log(n)), Space: O(1)

        st_map = {}
        for s in strs:
            st = str(sorted(s))
            if st not in st_map:
                st_map[st] = [s]
            else:
                st_map[st].append(s)

        rtn_lst = []
        for v in st_map.values():
            rtn_lst.append(v)

        return rtn_lst
