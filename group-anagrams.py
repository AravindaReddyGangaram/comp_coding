class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def countChar(lst1 : list, lst2: list):
            for ch in lst1:
                try:
                    lst2.remove(ch)
                except:
                    return False
            if len(lst2) == 0:
                return True
            return False
        def matchKey(dictionary : dict, string :str ):  #tea
            for keys in dictionary.keys():
                if len(keys) == len(string):
                    flag = countChar(list(keys), list(string))
                    if flag:
                        return keys
            return string
        final_list = [] # declaring the final_list to return
        dict_list = {} # declaring the dictionary to group the anagrams
        for string in strs:
            if string == "":
                if 'xyz1234xyz' in dict_list :
                    dict_list['xyz1234xyz'].append(string) 
                else :
                    dict_list['xyz1234xyz'] = [string]                      
            elif len(dict_list) == 0 :
                dict_list[string] =[string]
            else:
                matched_characters = matchKey(dict_list, string)
                if matched_characters in dict_list:
                    dict_list[matched_characters].append(string)
                else:
                    dict_list[matched_characters] = [matched_characters]
        for value in  dict_list.values():
            final_list.append(value)
        return final_list
