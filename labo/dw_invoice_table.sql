select top 1000
t.TrackId,
t.Name as titre,
g.Name as genre,
a.Title as 'album name',
t.Composer,
Milliseconds,
t.UnitPrice,
c.FirstName+' '+c.LastName as Customer,
e.FirstName+' '+e.LastName as Employee,
il.Quantity,
il.InvoiceId,
i.InvoiceDate,
i.BillingCity,
i.BillingCountry,
i.Total,
m.Name as media
from Track as t
join InvoiceLine as il on t.TrackId= il.TrackId
join Invoice as i on i.InvoiceId = il.InvoiceId
join Album as a on t.AlbumId = a.AlbumId
join MediaType	as m on t.MediaTypeId = t.MediaTypeId
join genre as g on g.GenreId=t.GenreId
join Customer as c on c.CustomerId = i.CustomerId
join Employee as e on e.EmployeeId = c.SupportRepId



