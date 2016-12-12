import win32com.client
adoConnection = win32com.client.Dispatch('ADODB.Connection')
adoCommand = win32com.client.Dispatch('ADODB.Command')
adoRecordset = win32com.client.Dispatch('ADODB.Recordset')
adoConnection.Provider = 'ADSDSOObject'
adoConnection.Properties('User ID').Value = 'jzhouja'
adoConnection.Properties('Password').Value = 'Qazwsx.,11'
adoConnection.Properties('Encrypt Password').Value = True
adoConnection.Properties('ADSI Flag').Value = 1
adoConnection.Open('Active Directory Provider')
adoCommand.ActiveConnection = adoConnection
adoCommand.Properties('Page Size').Value = 1000
ldap="SELECT cn, mail From 'LDAP://OU=Users,OU=CORP-China-Shanghai-877,OU=Sites,DC=asia,DC=jci,DC=com'"  # search statement
adoCommand.CommandText = ldap
adoRecordset.Open(adoCommand)
while not adoRecordset.EOF:
    print('{} {}'.format(adoRecordset('cn'), adoRecordset('mail'))) 
    adoRecordset.MoveNext()
adoRecordset.Close()
adoConnection.Close() 
