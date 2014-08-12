#coding=utf-8

_info_relation = {
        'user':{
            'relations':{
                'user':{
                    'fields':('username',)#'first_name','last_name','email','last_login')
                }
            },
            'fields':('user',)
        }
    }

_member_relation = {
    'user':{
        'fields':('username','first_name','last_name','email','last_login')
    },
    'location':{}
}
		