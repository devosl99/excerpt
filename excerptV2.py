#Luke De Vos
#EVL Labs
#Excerpt Extractor: Create directory and populate with excerpts#.txt between provided minimum and maximum length from given file
#To use:
#	python3 excerptV2.py [minLength] [MaxLength] [filePath]

import sys
import os
import queue

#command-line args
minLength=int(sys.argv[1])
maxLength=int(sys.argv[2])
filePath=sys.argv[3]

#other vars
fileNo=1
overMax=False
q = queue.Queue(maxsize=maxLength)					#to store words until conditions for writing excerpt are met
PUNCT_LIST=['.','?','!',';']
TITLE_LIST=["Mr.","Mrs.","Ms."]
snippet=filePath[0:len(filePath)-4]				#full path without trailing .txt	
fileName=os.path.basename(os.path.normpath(snippet))	#just file name, no path
outputDir="excerptV2.py_Output/"+fileName+"_Excerpts"

#===================================================================================================================

#Checks for end of sentence + queue's size being over minLength. Empties queue into excerpt file if so.
def check():
	global fileNo
	global overMax
	if lastChar in PUNCT_LIST and len(word) > 2 and word not in TITLE_LIST:
		if q.qsize()>=minLength:
			with open(outputDir+"/"+fileName+str(fileNo)+".txt", 'a') as out:	#file to be written to
				while q.empty()==False:								
					out.write(q.get() + " ")
			if overMax==False:					
				fileNo+=1
		overMax=False
	return

#execution
os.makedirs(outputDir, exist_ok=True)		#create folder to hold excerpts
with open(filePath) as f:
	for line in f:
		for word in line.split():
			if q.qsize() >= maxLength:
				overMax=True			#overMax is changed to False in check() when the end of a sentence is found.
									#once that happens, normal queue filling resumes
				print(fileName+str(fileNo)+" draft deleted due to length.")			
				q.queue.clear()
			else:
				if overMax==False:		
					q.put(word)		
				lastChar=word[len(word)-1]
				check()
				if lastChar in ["\"","\'"]:
					lastChar=word[len(word)-2]		
					check()
					
print("-"+fileName+".txt Processed-")



