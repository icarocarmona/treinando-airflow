
def first_function_execute(**context):
    variable = context.get("name", "Didnt not get the key")
    print('@'*66)
    print("Hello {}".format(variable))
    context['ti'].xcom_push(key='name_key', value='Push value Icaro Almeida') # ti = taskinstance
