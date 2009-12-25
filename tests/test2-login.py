import CTK

LOGINS = {
    'root': "god",
    'alo' : "cherokee"
}

def apply (post):
    name  = post.get_val('login!name')
    passw = post.get_val('login!pass')

    if not name in LOGINS:
        return {'ret': "error", 'errors': {'login!name': "Unknown user"}}
    if LOGINS[name] != passw:
        return {'ret': "error", 'errors': {'login!pass': "Wrong password"}}

    return {'ret': "ok"}


class default:
    def __init__ (self):
        g = CTK.PropsTable()
        g.Add ('User',     CTK.TextField({'name': "login!name", 'class': "required"}), 'Type your user name')
        g.Add ('Password', CTK.TextField({'name': "login!pass", 'class': "required"}), 'Type your password')

        form = CTK.Submitter("/apply")
        form += g

        self.page = CTK.Page()
        self.page += form

    def __call__ (self):
        return self.page.Render()


CTK.publish ('/apply', apply, method="POST")
CTK.publish ('', default)

CTK.run (port=8000)