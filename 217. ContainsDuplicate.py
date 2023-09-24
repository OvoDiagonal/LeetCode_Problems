lass Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        #Iterates trough the numbers adding them to the hashmap and verifiyng if the number is a duplicate
        for n in nums:
          if n in hashset:
            return True

          hashset.add(n)
        #If the iteration ends and there are no Duplicates it returns False
        return False
