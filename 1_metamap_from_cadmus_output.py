import pandas as pd
import pickle
import re
from pathlib import Path
import subprocess
import multiprocessing


# define which text col to process - tiab or content_text
mm_col = 'tiab'

# define output dir
output_dir = "path_to_output_dir"

# define cwd
mm_cwd = "path_to_cwd"

# define no cores to use

n_processes = 10

def removeNonAscii(s):
    return "".join(filter(lambda x: ord(x)<128, s))

def metamap_run(arg):
    file_id, content_str = arg
    print (f'processing {file_id}')
#     metamap options here
    mm_cmd = ['metamap',  '-N',  '-R',  'HPO']
    with open(f"{output_dir}{file_id}.out", "wb") as outfile:
        subprocess.run(mm_cmd, 
                       cwd=mm_cwd, 
                       text=True, 
                       input=content_str, 
                       stdout=outfile)

mm_output_dir = Path(output_dir)
mm_output_indices = [i.stem for i in mm_output_dir.glob('*.out')]

ret_df = pickle.load(open('path_to_cadmus_retdf2','rb'))
ret_df = ret_df.dropna(subset=['title','abstract','content_text'])
# only process files without existing metamap output
ret_df = ret_df[~ret_df.index.isin(mm_output_indices)]
# ret_df['technical_text'] = [removeNonAscii(i) for i in ret_df['technical_text']]
ret_df['content_text'] = [removeNonAscii(i) for i in ret_df['content_text']]
ret_df['title'] = [removeNonAscii(i) for i in ret_df['title']]
ret_df['abstract'] = [removeNonAscii(i) for i in ret_df['abstract']]
ret_df['tiab'] = ret_df['title'] + ' ' + ret_df['abstract']


mm_inputs = list(zip(ret_df.index, ret_df[mm_col]))

# make sure processes is less than available no cores
pool = multiprocessing.Pool(processes=n_processes)
pool.imap(metamap_run, mm_inputs)
pool.close()
pool.join()
