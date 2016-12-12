import IEC,re
ie=IEC.IEController()
ie.Navigate('http://directory.corp.jci.com/PersonDetail.aspx?uid=ccheunan')
info=ie.GetDocumentText()
info=info.replace('|',' ')
p=re.compile(r' \r\n \r\n Global Directory\r\nPeople   Locations   Update Me   Help \r\nSimple Search Advanced Search Person Details \r\n\r\n\r\n(?P<name>[A-Z][a-zA-Z ]*[A-Za-z])\r\n\r\n\r\nEmployee\r\nJob Title: Systems Project Manager  \r\nSelf-managed Title:   \r\nBusiness Unit:\s+(?P<bu>[a-zA-Z]*)\s+\r\nDepartment: Hong Kong Systems  \r\nGlobal ID: ccheunan  \r\n\r\n\r\nBusiness Contact Information\r\nPhone:   \r\nGlobal Dialing:   \r\nMobile:   \r\nPager:   \r\nFax:   \r\nEmail: Anthony.KH.Cheung@jci.com  \r\nHR Location:\s+(?P<location>[a-zA-Z ]*)\s+\r\n  20/F Tower 1 2 & 3 Enterprise Square 1\r\n18 Sheung Yuet Road\r\n\r\n  Kowloon Bay K \r\n  Hong Kong \r\nMail Station:   \r\nAlt. Business Phone:   \r\nAlt. Business Address:   \r\n    \r\n    \r\n    \r\nIT Access Location: BE Hong Kong  \r\n\r\n\r\nReporting Structure\r\nReports To: Kok Wai Chuk   \r\n  Employees Reporting to Kam Ho Cheung      \r\nAssistant:   \r\nLast Modified: 7/3/2012 3:02:15 AM\r\nPrivacy   Terms of Use   Copyright ')
s=p.search(info).group(1,2,3)
print(s)

