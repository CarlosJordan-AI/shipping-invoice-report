-- Report: Invoiced shipments by carrier/factory from a start date
-- Shape: Orders ↔ Packages; realistic filters (carrier, site, start date)
SELECT 
    o.id,
    o.xid,
    sp.trackingnumber,
    o.CustomPartnerId,
    o.SortedOnUtc,
    o.TotalWeightLbs,
    o.ShippingBase,
    o.ShippingAmount,
    o.FactoryId,
    o.ShippingPriority,
    o.IsInvoiced,
    o.InvoiceWeek
FROM "order" o
JOIN "shippackage" sp ON sp.orderid = o.id
WHERE 
    o.IsShippingInvoiced = 1
    AND o.IsInvoiced = 1
    AND o.ShippingCarrier = :carrier
    AND o.SortedOnUtc >= :start
    AND o.FactoryId = :factory
ORDER BY o.SortedOnUtc ASC, o.id ASC;
