def bubbleSort(nums):
    for i in range(len(nums) -1):
        for j in range(0, len(nums) - i -1):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp

def insertSort(nums):
    for i in range(1,len(nums)):
        if nums[i] < nums[i-1]:
            num = nums[i]
            j = i-1
            while j >= 0 and nums[j]> num:
                nums[j+1] = nums[j]
                j -= 1
            nums[j + 1] = num

nums = [1,3,2,5,6,0]
insertSort(nums)
print nums

en_key_words = ['Associate Professor', 'Assistant Professor', 'Professor Emeritus', 'associate professor',
     'Distinguished Professor', 'Senior Lecturer', 'assistant professor', 'Research Fellow', 'Associate professor',
     'Chair Professor', 'Research Professor', 'Emeritus Professor', 'Full Professor', 'Prof.', 'Principal Investigator',
     'Adjunct Professor', 'Full professor', 'Vice President', 'Research Assistant Professor', 'ASSOCIATE PROFESSOR',
     'Associate Dean', 'Senior Researcher', 'Research Associate', 'Associate Director', 'full professor',
     'Associate Head', 'Co-Director', 'Assistant professor', 'Research Scientist', 'Assistant Dean', 'Doctoral Advisor',
     'Research Associate Professor', 'ASSISTANT PROFESSOR', 'Executive Director', 'Teaching Fellow', 'Chief Scientist',
     'Senior Research Scientist', 'Professor', 'professor', 'Director', 'Lecturer', 'PROFESSOR', 'Professor', 'Chair',
     'CEO', 'Prof', 'Reader', 'Dean', ' Director', 'director', 'Fellow', 'president', 'Head', 'President',
     'Researcher', 'Chairman', 'Investigator','researcher']

en_key_words = [word.strip() for word in en_key_words]

print en_key_words