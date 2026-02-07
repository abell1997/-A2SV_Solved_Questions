
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_map = {}

        for path in paths:
            parts = path.split()
            directory = parts[0]

            for file_info in parts[1:]:
                file_name, content = file_info.split('(')
                content = content[:-1]

                if content not in content_map:
                    content_map[content] = []
                content_map[content].append(directory + '/' + file_name)
            
        duplicates = []
        for files in content_map.values():
            if len(files) > 1:
                duplicates.append(files)
                
        return duplicates
        