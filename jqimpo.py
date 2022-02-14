import pyjq
var = data = dict(parameters= [
dict(name="PKG_TAG_NAME", value="trunk"),
dict(name="GIT_COMMIT", value="master"),
dict(name="TRIGGERED_JOB", value="trunk-buildall")],id="2013-12-27_00-09-37",changeSet=dict(items=[], kind="git"),)
jqcll=pyjq.first('.parameters[] | {"param_name": .name, "param_type":.type}', data)
{'param_name': 'PKG_TAG_NAME', 'param_type': None}
value = {"user":"stedolan","titles":["JQ Primer", "More JQ"]}
pyjq.all('{user, title: .titles[]}', value)
[{'user': 'stedolan', 'title': 'JQ Primer'}, {'user': 'stedolan', 'title': 'More JQ'}]
print(value)