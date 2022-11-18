import glob
import json
import os

def readme(f):
	readme_pth = os.path.join(*f_split[:-1], "README_" + f_split[-1] + ".txt")
	if os.path.isfile(readme_pth):
		with open(readme_pth, "r") as r:
			content = r.read()
		return content
	else:
		return None

files_list = glob.glob("**/*.jinja", recursive=True)

tpls = {}
for f in files_list:
	# print(f)
	f_split = f.split("/")
	basename, ext = os.path.splitext(f)
	f_split = basename.split("/")
	f_split
	tpl_name = f_split[-1]
	tpls[tpl_name] = {
		"url": f,
		"description": readme(f)
	}

print(json.dumps(tpls, indent=4))
