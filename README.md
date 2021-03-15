"# GraphQl-Authentication" 

pip install -r requirement.txt

python manage.py makemigrations

python manage.py migrate

python manage.py seed users --number=15

python manage.py runserver





         Register
============================

        mutation
        {
        register(input:{email:"",username:"",password1:"",password2:""})
            {
            success
            errors
            token
            refreshToken
        }
        }



         Verify Token
===============================

        mutation{
        verifyToken(input:{token:""})
        {
            success
            errors
            __typename
        }
        }



           Users
===============================


        query{
        users{
            edges{
            node{
                id
                username
                email
                isStaff
                isSuperuser
                firstName
                lastName
                lastName
                isActive
                lastLogin
            }
            }
        }
        }
