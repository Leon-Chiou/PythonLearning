import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import*

#Import DocumentManager
clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

# Import RevitAPI
clr.AddReference("RevitAPI")
import Autodesk

# Import ToDSType(bool) extension method
clr.AddReference("RevitNodes")
import Revit
from Autodesk.Revit.DB import*
from Autodesk.Revit.Creation import*
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)

# The inputs to this node will be stored as a list in the IN variable

FirstPoint = IN[0]
SecondPoint = IN[1]
pipetype = UnwrapElement(IN[2])
systemtype = UnwrapElement(IN[3])
level = UnwrapElement(IN[4])
doc = IN[5]

LevelId = level.Id
elements = []

TransactionManager.Instance.EnsureInTrasaction(doc)

for i,x in enumerate(FirstPoint):
    pipe = Autodesk.Revit.DB.Plumbing.Pipe.Create(doc, systemtype.Id, pipetype.Id, LevelId, FirstPoint[i].ToXyz(), SecondPoint[i].ToXyz())
    elements.append(pipe.Id)

TransactionManager.Instance.trasactionTaskDone()

OUT = elements