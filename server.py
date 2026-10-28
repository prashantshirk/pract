import json, base64

SECTIONS = json.loads(base64.b64decode((
    "W3sidGl0bGUiOiAiLk5FVCBQcmFjdGljYWxzIiwgIml0ZW1zIjogW3sibmFtZSI6ICJBY2NvdW50"
    "QmFsYW5jZSIsICJhaW0iOiAiQ29uc29sZSBhcHAgdXNpbmcgYSBwcm9wZXJ0eSB3aXRoIHZhbGlk"
    "YXRpb24sIHNvIGFuIGFjY291bnQgYmFsYW5jZSBjYW5ub3QgZ28gbmVnYXRpdmUuIiwgInNvZnR3"
    "YXJlIjogIlZpc3VhbCBTdHVkaW8gLyAuTkVUIiwgInN0ZXBzIjogIkRvd25sb2FkIHRoZSB6aXAs"
    "IGV4dHJhY3QgaXQsIHRoZW4gb3BlbiB0aGUgc29sdXRpb24gZmlsZSBpbnNpZGUgaW4gVmlzdWFs"
    "IFN0dWRpby4iLCAiZmlsZXMiOiBbXSwgInJ1biI6ICJFeHRyYWN0IHRoZSB6aXAgYW5kIG9wZW4g"
    "dGhlIHNvbHV0aW9uIGluIFZpc3VhbCBTdHVkaW8sIHRoZW4gcnVuIHRoZSBwcm9qZWN0LiIsICJk"
    "b3dubG9hZCI6ICJodHRwczovL3Jhdy5naXRodWJ1c2VyY29udGVudC5jb20vcHJhc2hhbnRzaGly"
    "ay9wcmFjdC9tYWluL2RvdG5ldC16aXBzL0FjY291bnRCYWxhbmNlLnppcCJ9LCB7Im5hbWUiOiAi"
    "QWRyb3RhdG9yIiwgImFpbSI6ICJBU1AuTkVUIFdlYiBGb3JtcyBwYWdlIHRoYXQgcm90YXRlcyBh"
    "ZHMgZnJvbSBhbiBYTUwgZmlsZSB1c2luZyB0aGUgQWRSb3RhdG9yIGNvbnRyb2wuIiwgInNvZnR3"
    "YXJlIjogIlZpc3VhbCBTdHVkaW8gLyAuTkVUIiwgInN0ZXBzIjogIkRvd25sb2FkIHRoZSB6aXAs"
    "IGV4dHJhY3QgaXQsIHRoZW4gb3BlbiB0aGUgc29sdXRpb24gZmlsZSBpbnNpZGUgaW4gVmlzdWFs"
    "IFN0dWRpby4iLCAiZmlsZXMiOiBbXSwgInJ1biI6ICJFeHRyYWN0IHRoZSB6aXAgYW5kIG9wZW4g"
    "dGhlIHNvbHV0aW9uIGluIFZpc3VhbCBTdHVkaW8sIHRoZW4gcnVuIHRoZSBwcm9qZWN0LiIsICJk"
    "b3dubG9hZCI6ICJodHRwczovL3Jhdy5naXRodWJ1c2VyY29udGVudC5jb20vcHJhc2hhbnRzaGly"
    "ay9wcmFjdC9tYWluL2RvdG5ldC16aXBzL0Fkcm90YXRvci56aXAifSwgeyJuYW1lIjogIkF1dGhl"
    "bnRpY2F0aW9uYW5kYXV0aG9yaXphdGlvbiIsICJhaW0iOiAiQVNQLk5FVCBDb3JlIE1WQyBhcHAg"
    "d2l0aCBJZGVudGl0eSBsb2dpbiwgcGx1cyBhIHByb3RlY3RlZCBTZWNyZXQgcGFnZSB0aGF0IHNo"
    "b3dzIGF1dGhlbnRpY2F0aW9uIGFuZCBhdXRob3JpemF0aW9uLiIsICJzb2Z0d2FyZSI6ICJWaXN1"
    "YWwgU3R1ZGlvIC8gLk5FVCIsICJzdGVwcyI6ICJEb3dubG9hZCB0aGUgemlwLCBleHRyYWN0IGl0"
    "LCB0aGVuIG9wZW4gdGhlIHNvbHV0aW9uIGZpbGUgaW5zaWRlIGluIFZpc3VhbCBTdHVkaW8uIiwg"
    "ImZpbGVzIjogW10sICJydW4iOiAiRXh0cmFjdCB0aGUgemlwIGFuZCBvcGVuIHRoZSBzb2x1dGlv"
    "biBpbiBWaXN1YWwgU3R1ZGlvLCB0aGVuIHJ1biB0aGUgcHJvamVjdC4iLCAiZG93bmxvYWQiOiAi"
    "aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL3ByYXNoYW50c2hpcmsvcHJhY3QvbWFp"
    "bi9kb3RuZXQtemlwcy9BdXRoZW50aWNhdGlvbmFuZGF1dGhvcml6YXRpb24uemlwIn0sIHsibmFt"
    "ZSI6ICJDb2xsZWdlUFdBIiwgImFpbSI6ICJQcm9ncmVzc2l2ZSB3ZWIgYXBwIGZvciBhIGNvbGxl"
    "Z2Ugc2l0ZSwgd2l0aCBhIG1hbmlmZXN0IGFuZCBzZXJ2aWNlIHdvcmtlciBzbyBpdCBjYW4gYmUg"
    "aW5zdGFsbGVkLiIsICJzb2Z0d2FyZSI6ICJWaXN1YWwgU3R1ZGlvIC8gLk5FVCIsICJzdGVwcyI6"
    "ICJEb3dubG9hZCB0aGUgemlwLCBleHRyYWN0IGl0LCB0aGVuIG9wZW4gdGhlIHNvbHV0aW9uIGZp"
    "bGUgaW5zaWRlIGluIFZpc3VhbCBTdHVkaW8uIiwgImZpbGVzIjogW10sICJydW4iOiAiRXh0cmFj"
    "dCB0aGUgemlwIGFuZCBvcGVuIHRoZSBzb2x1dGlvbiBpbiBWaXN1YWwgU3R1ZGlvLCB0aGVuIHJ1"
    "biB0aGUgcHJvamVjdC4iLCAiZG93bmxvYWQiOiAiaHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRl"
    "bnQuY29tL3ByYXNoYW50c2hpcmsvcHJhY3QvbWFpbi9kb3RuZXQtemlwcy9Db2xsZWdlUFdBLnpp"
    "cCJ9LCB7Im5hbWUiOiAiQ29uc3RydWN0b3JzIiwgImFpbSI6ICJDb25zb2xlIGFwcCBzaG93aW5n"
    "IGRlZmF1bHQgYW5kIHBhcmFtZXRlcml6ZWQgY29uc3RydWN0b3JzIHdpdGggYSBzdHVkZW50IGNs"
    "YXNzLiIsICJzb2Z0d2FyZSI6ICJWaXN1YWwgU3R1ZGlvIC8gLk5FVCIsICJzdGVwcyI6ICJEb3du"
    "bG9hZCB0aGUgemlwLCBleHRyYWN0IGl0LCB0aGVuIG9wZW4gdGhlIHNvbHV0aW9uIGZpbGUgaW5z"
    "aWRlIGluIFZpc3VhbCBTdHVkaW8uIiwgImZpbGVzIjogW10sICJydW4iOiAiRXh0cmFjdCB0aGUg"
    "emlwIGFuZCBvcGVuIHRoZSBzb2x1dGlvbiBpbiBWaXN1YWwgU3R1ZGlvLCB0aGVuIHJ1biB0aGUg"
    "cHJvamVjdC4iLCAiZG93bmxvYWQiOiAiaHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29t"
    "L3ByYXNoYW50c2hpcmsvcHJhY3QvbWFpbi9kb3RuZXQtemlwcy9Db25zdHJ1Y3RvcnMuemlwIn0s"
    "IHsibmFtZSI6ICJDb29raWVzIiwgImFpbSI6ICJBU1AuTkVUIFdlYiBGb3JtcyBhcHAgc2hvd2lu"
    "ZyBob3cgY29va2llcyBzdG9yZSBhbmQgcmVhZCB1c2VyIGRhdGEgYWNyb3NzIHJlcXVlc3RzLiIs"
    "ICJzb2Z0d2FyZSI6ICJWaXN1YWwgU3R1ZGlvIC8gLk5FVCIsICJzdGVwcyI6ICJEb3dubG9hZCB0"
    "aGUgemlwLCBleHRyYWN0IGl0LCB0aGVuIG9wZW4gdGhlIHNvbHV0aW9uIGZpbGUgaW5zaWRlIGlu"
    "IFZpc3VhbCBTdHVkaW8uIiwgImZpbGVzIjogW10sICJydW4iOiAiRXh0cmFjdCB0aGUgemlwIGFu"
    "ZCBvcGVuIHRoZSBzb2x1dGlvbiBpbiBWaXN1YWwgU3R1ZGlvLCB0aGVuIHJ1biB0aGUgcHJvamVj"
    "dC4iLCAiZG93bmxvYWQiOiAiaHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL3ByYXNo"
    "YW50c2hpcmsvcHJhY3QvbWFpbi9kb3RuZXQtemlwcy9Db29raWVzLnppcCJ9LCB7Im5hbWUiOiAi"
    "Q291cnNlcyIsICJhaW0iOiAiQVNQLk5FVCBXZWIgRm9ybXMgc3R1ZGVudCBmb3JtIGFwcC4iLCAi"
    "c29mdHdhcmUiOiAiVmlzdWFsIFN0dWRpbyAvIC5ORVQiLCAic3RlcHMiOiAiRG93bmxvYWQgdGhl"
    "IHppcCwgZXh0cmFjdCBpdCwgdGhlbiBvcGVuIHRoZSBzb2x1dGlvbiBmaWxlIGluc2lkZSBpbiBW"
    "aXN1YWwgU3R1ZGlvLiIsICJmaWxlcyI6IFtdLCAicnVuIjogIkV4dHJhY3QgdGhlIHppcCBhbmQg"
    "b3BlbiB0aGUgc29sdXRpb24gaW4gVmlzdWFsIFN0dWRpbywgdGhlbiBydW4gdGhlIHByb2plY3Qu"
    "IiwgImRvd25sb2FkIjogImh0dHBzOi8vcmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbS9wcmFzaGFu"
    "dHNoaXJrL3ByYWN0L21haW4vZG90bmV0LXppcHMvQ291cnNlcy56aXAifSwgeyJuYW1lIjogIkRl"
    "bGVnYXRlcyIsICJhaW0iOiAiQ29uc29sZSBhcHAgc2hvd2luZyBzaW5nbGUtY2FzdCBkZWxlZ2F0"
    "ZXMgY2FsbGluZyBhZGQsIHN1YnRyYWN0LCBtdWx0aXBseSBhbmQgZGl2aWRlIG1ldGhvZHMuIiwg"
    "InNvZnR3YXJlIjogIlZpc3VhbCBTdHVkaW8gLyAuTkVUIiwgInN0ZXBzIjogIkRvd25sb2FkIHRo"
    "ZSB6aXAsIGV4dHJhY3QgaXQsIHRoZW4gb3BlbiB0aGUgc29sdXRpb24gZmlsZSBpbnNpZGUgaW4g"
    "VmlzdWFsIFN0dWRpby4iLCAiZmlsZXMiOiBbXSwgInJ1biI6ICJFeHRyYWN0IHRoZSB6aXAgYW5k"
    "IG9wZW4gdGhlIHNvbHV0aW9uIGluIFZpc3VhbCBTdHVkaW8sIHRoZW4gcnVuIHRoZSBwcm9qZWN0"
    "LiIsICJkb3dubG9hZCI6ICJodHRwczovL3Jhdy5naXRodWJ1c2VyY29udGVudC5jb20vcHJhc2hh"
    "bnRzaGlyay9wcmFjdC9tYWluL2RvdG5ldC16aXBzL0RlbGVnYXRlcy56aXAifSwgeyJuYW1lIjog"
    "IkVDb21tZXJjZSIsICJhaW0iOiAiQVNQLk5FVCBhcHAgd2l0aCBhIHdlYiBzdG9yZSBmcm9udC1l"
    "bmQsIGluY2x1ZGluZyBhIG1hbmlmZXN0IGFuZCBzZXJ2aWNlIHdvcmtlci4iLCAic29mdHdhcmUi"
    "OiAiVmlzdWFsIFN0dWRpbyAvIC5ORVQiLCAic3RlcHMiOiAiRG93bmxvYWQgdGhlIHppcCwgZXh0"
    "cmFjdCBpdCwgdGhlbiBvcGVuIHRoZSBzb2x1dGlvbiBmaWxlIGluc2lkZSBpbiBWaXN1YWwgU3R1"
    "ZGlvLiIsICJmaWxlcyI6IFtdLCAicnVuIjogIkV4dHJhY3QgdGhlIHppcCBhbmQgb3BlbiB0aGUg"
    "c29sdXRpb24gaW4gVmlzdWFsIFN0dWRpbywgdGhlbiBydW4gdGhlIHByb2plY3QuIiwgImRvd25s"
    "b2FkIjogImh0dHBzOi8vcmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbS9wcmFzaGFudHNoaXJrL3By"
    "YWN0L21haW4vZG90bmV0LXppcHMvRUNvbW1lcmNlLnppcCJ9LCB7Im5hbWUiOiAiRW1wbG95ZWVD"
    "UlVEIiwgImFpbSI6ICJBU1AuTkVUIGFwcCBmb3IgY3JlYXRpbmcsIHJlYWRpbmcsIHVwZGF0aW5n"
    "IGFuZCBkZWxldGluZyBlbXBsb3llZSByZWNvcmRzLiIsICJzb2Z0d2FyZSI6ICJWaXN1YWwgU3R1"
    "ZGlvIC8gLk5FVCIsICJzdGVwcyI6ICJEb3dubG9hZCB0aGUgemlwLCBleHRyYWN0IGl0LCB0aGVu"
    "IG9wZW4gdGhlIHNvbHV0aW9uIGZpbGUgaW5zaWRlIGluIFZpc3VhbCBTdHVkaW8uIiwgImZpbGVz"
    "IjogW10sICJydW4iOiAiRXh0cmFjdCB0aGUgemlwIGFuZCBvcGVuIHRoZSBzb2x1dGlvbiBpbiBW"
    "aXN1YWwgU3R1ZGlvLCB0aGVuIHJ1biB0aGUgcHJvamVjdC4iLCAiZG93bmxvYWQiOiAiaHR0cHM6"
    "Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL3ByYXNoYW50c2hpcmsvcHJhY3QvbWFpbi9kb3Ru"
    "ZXQtemlwcy9FbXBsb3llZUNSVUQuemlwIn0sIHsibmFtZSI6ICJGT0xZRHMiLCAiYWltIjogIkNv"
    "bnNvbGUgYXBwIHByaW50aW5nIGEgRmxveWQtc3R5bGUgdHJpYW5nbGUgbnVtYmVyIHBhdHRlcm4u"
    "IiwgInNvZnR3YXJlIjogIlZpc3VhbCBTdHVkaW8gLyAuTkVUIiwgInN0ZXBzIjogIkRvd25sb2Fk"
    "IHRoZSB6aXAsIGV4dHJhY3QgaXQsIHRoZW4gb3BlbiB0aGUgc29sdXRpb24gZmlsZSBpbnNpZGUg"
    "aW4gVmlzdWFsIFN0dWRpby4iLCAiZmlsZXMiOiBbXSwgInJ1biI6ICJFeHRyYWN0IHRoZSB6aXAg"
    "YW5kIG9wZW4gdGhlIHNvbHV0aW9uIGluIFZpc3VhbCBTdHVkaW8sIHRoZW4gcnVuIHRoZSBwcm9q"
    "ZWN0LiIsICJkb3dubG9hZCI6ICJodHRwczovL3Jhdy5naXRodWJ1c2VyY29udGVudC5jb20vcHJh"
    "c2hhbnRzaGlyay9wcmFjdC9tYWluL2RvdG5ldC16aXBzL0ZPTFlEcy56aXAifSwgeyJuYW1lIjog"
    "IkZhY3RvcmlhbENvbnRyb2xsZXIiLCAiYWltIjogIkFTUC5ORVQgQ29yZSBBUEkgd2hlcmUgYSBN"
    "YXRoIGNvbnRyb2xsZXIgY2FsY3VsYXRlcyBhIGZhY3RvcmlhbC4iLCAic29mdHdhcmUiOiAiVmlz"
    "dWFsIFN0dWRpbyAvIC5ORVQiLCAic3RlcHMiOiAiRG93bmxvYWQgdGhlIHppcCwgZXh0cmFjdCBp"
    "dCwgdGhlbiBvcGVuIHRoZSBzb2x1dGlvbiBmaWxlIGluc2lkZSBpbiBWaXN1YWwgU3R1ZGlvLiIs"
    "ICJmaWxlcyI6IFtdLCAicnVuIjogIkV4dHJhY3QgdGhlIHppcCBhbmQgb3BlbiB0aGUgc29sdXRp"
    "b24gaW4gVmlzdWFsIFN0dWRpbywgdGhlbiBydW4gdGhlIHByb2plY3QuIiwgImRvd25sb2FkIjog"
    "Imh0dHBzOi8vcmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbS9wcmFzaGFudHNoaXJrL3ByYWN0L21h"
    "aW4vZG90bmV0LXppcHMvRmFjdG9yaWFsQ29udHJvbGxlci56aXAifSwgeyJuYW1lIjogIkZ1bmN0"
    "aW9uT3ZlcmxvYWRpbmdzIiwgImFpbSI6ICJDb25zb2xlIGFwcCBzaG93aW5nIG1ldGhvZCBvdmVy"
    "bG9hZGluZyB3aXRoIGRpZmZlcmVudCBudW1iZXJzIGFuZCB0eXBlcyBvZiBhcmd1bWVudHMuIiwg"
    "InNvZnR3YXJlIjogIlZpc3VhbCBTdHVkaW8gLyAuTkVUIiwgInN0ZXBzIjogIkRvd25sb2FkIHRo"
    "ZSB6aXAsIGV4dHJhY3QgaXQsIHRoZW4gb3BlbiB0aGUgc29sdXRpb24gZmlsZSBpbnNpZGUgaW4g"
    "VmlzdWFsIFN0dWRpby4iLCAiZmlsZXMiOiBbXSwgInJ1biI6ICJFeHRyYWN0IHRoZSB6aXAgYW5k"
    "IG9wZW4gdGhlIHNvbHV0aW9uIGluIFZpc3VhbCBTdHVkaW8sIHRoZW4gcnVuIHRoZSBwcm9qZWN0"
    "LiIsICJkb3dubG9hZCI6ICJodHRwczovL3Jhdy5naXRodWJ1c2VyY29udGVudC5jb20vcHJhc2hh"
    "bnRzaGlyay9wcmFjdC9tYWluL2RvdG5ldC16aXBzL0Z1bmN0aW9uT3ZlcmxvYWRpbmdzLnppcCJ9"
    "LCB7Im5hbWUiOiAiSW5oZXJpdGVuY2UiLCAiYWltIjogIkNvbnNvbGUgYXBwIHNob3dpbmcgbXVs"
    "dGlsZXZlbCBpbmhlcml0YW5jZSB3aXRoIHBhcmVudCBhbmQgY2hpbGQgY2xhc3Nlcy4iLCAic29m"
    "dHdhcmUiOiAiVmlzdWFsIFN0dWRpbyAvIC5ORVQiLCAic3RlcHMiOiAiRG93bmxvYWQgdGhlIHpp"
    "cCwgZXh0cmFjdCBpdCwgdGhlbiBvcGVuIHRoZSBzb2x1dGlvbiBmaWxlIGluc2lkZSBpbiBWaXN1"
    "YWwgU3R1ZGlvLiIsICJmaWxlcyI6IFtdLCAicnVuIjogIkV4dHJhY3QgdGhlIHppcCBhbmQgb3Bl"
    "biB0aGUgc29sdXRpb24gaW4gVmlzdWFsIFN0dWRpbywgdGhlbiBydW4gdGhlIHByb2plY3QuIiwg"
    "ImRvd25sb2FkIjogImh0dHBzOi8vcmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbS9wcmFzaGFudHNo"
    "aXJrL3ByYWN0L21haW4vZG90bmV0LXppcHMvSW5oZXJpdGVuY2UuemlwIn0sIHsibmFtZSI6ICJJ"
    "bnRlcmZhY2UiLCAiYWltIjogIkNvbnNvbGUgYXBwIHNob3dpbmcgYW4gaW50ZXJmYWNlIGltcGxl"
    "bWVudGVkIGJ5IGEgc2hhcGUgY2xhc3MuIiwgInNvZnR3YXJlIjogIlZpc3VhbCBTdHVkaW8gLyAu"
    "TkVUIiwgInN0ZXBzIjogIkRvd25sb2FkIHRoZSB6aXAsIGV4dHJhY3QgaXQsIHRoZW4gb3BlbiB0"
    "aGUgc29sdXRpb24gZmlsZSBpbnNpZGUgaW4gVmlzdWFsIFN0dWRpby4iLCAiZmlsZXMiOiBbXSwg"
    "InJ1biI6ICJFeHRyYWN0IHRoZSB6aXAgYW5kIG9wZW4gdGhlIHNvbHV0aW9uIGluIFZpc3VhbCBT"
    "dHVkaW8sIHRoZW4gcnVuIHRoZSBwcm9qZWN0LiIsICJkb3dubG9hZCI6ICJodHRwczovL3Jhdy5n"
    "aXRodWJ1c2VyY29udGVudC5jb20vcHJhc2hhbnRzaGlyay9wcmFjdC9tYWluL2RvdG5ldC16aXBz"
    "L0ludGVyZmFjZS56aXAifSwgeyJuYW1lIjogIk11bHRpY2FzdERlbGVnYXRlcyIsICJhaW0iOiAi"
    "Q29uc29sZSBhcHAgc2hvd2luZyBhIG11bHRpY2FzdCBkZWxlZ2F0ZSBjYWxsaW5nIHNldmVyYWwg"
    "bWV0aG9kcyBpbiBvbmUgaW52b2NhdGlvbi4iLCAic29mdHdhcmUiOiAiVmlzdWFsIFN0dWRpbyAv"
    "IC5ORVQiLCAic3RlcHMiOiAiRG93bmxvYWQgdGhlIHppcCwgZXh0cmFjdCBpdCwgdGhlbiBvcGVu"
    "IHRoZSBzb2x1dGlvbiBmaWxlIGluc2lkZSBpbiBWaXN1YWwgU3R1ZGlvLiIsICJmaWxlcyI6IFtd"
    "LCAicnVuIjogIkV4dHJhY3QgdGhlIHppcCBhbmQgb3BlbiB0aGUgc29sdXRpb24gaW4gVmlzdWFs"
    "IFN0dWRpbywgdGhlbiBydW4gdGhlIHByb2plY3QuIiwgImRvd25sb2FkIjogImh0dHBzOi8vcmF3"
    "LmdpdGh1YnVzZXJjb250ZW50LmNvbS9wcmFzaGFudHNoaXJrL3ByYWN0L21haW4vZG90bmV0LXpp"
    "cHMvTXVsdGljYXN0RGVsZWdhdGVzLnppcCJ9LCB7Im5hbWUiOiAiT2ZmbGluZVBXQSIsICJhaW0i"
    "OiAiUHJvZ3Jlc3NpdmUgd2ViIGFwcCB0aGF0IHdvcmtzIG9mZmxpbmUsIHdpdGggYSBzZXJ2aWNl"
    "IHdvcmtlciBhbmQgY2FjaGUuIiwgInNvZnR3YXJlIjogIlZpc3VhbCBTdHVkaW8gLyAuTkVUIiwg"
    "InN0ZXBzIjogIkRvd25sb2FkIHRoZSB6aXAsIGV4dHJhY3QgaXQsIHRoZW4gb3BlbiB0aGUgc29s"
    "dXRpb24gZmlsZSBpbnNpZGUgaW4gVmlzdWFsIFN0dWRpby4iLCAiZmlsZXMiOiBbXSwgInJ1biI6"
    "ICJFeHRyYWN0IHRoZSB6aXAgYW5kIG9wZW4gdGhlIHNvbHV0aW9uIGluIFZpc3VhbCBTdHVkaW8s"
    "IHRoZW4gcnVuIHRoZSBwcm9qZWN0LiIsICJkb3dubG9hZCI6ICJodHRwczovL3Jhdy5naXRodWJ1"
    "c2VyY29udGVudC5jb20vcHJhc2hhbnRzaGlyay9wcmFjdC9tYWluL2RvdG5ldC16aXBzL09mZmxp"
    "bmVQV0EuemlwIn0sIHsibmFtZSI6ICJQV0FMSU5LTUFuaWZlc3QiLCAiYWltIjogIlBXQSBleGFt"
    "cGxlIGZvY3VzZWQgb24gdGhlIHdlYiBhcHAgbWFuaWZlc3QgYW5kIGxpbmtpbmcgaXQgaW50byB0"
    "aGUgc2l0ZS4iLCAic29mdHdhcmUiOiAiVmlzdWFsIFN0dWRpbyAvIC5ORVQiLCAic3RlcHMiOiAi"
    "RG93bmxvYWQgdGhlIHppcCwgZXh0cmFjdCBpdCwgdGhlbiBvcGVuIHRoZSBzb2x1dGlvbiBmaWxl"
    "IGluc2lkZSBpbiBWaXN1YWwgU3R1ZGlvLiIsICJmaWxlcyI6IFtdLCAicnVuIjogIkV4dHJhY3Qg"
    "dGhlIHppcCBhbmQgb3BlbiB0aGUgc29sdXRpb24gaW4gVmlzdWFsIFN0dWRpbywgdGhlbiBydW4g"
    "dGhlIHByb2plY3QuIiwgImRvd25sb2FkIjogImh0dHBzOi8vcmF3LmdpdGh1YnVzZXJjb250ZW50"
    "LmNvbS9wcmFzaGFudHNoaXJrL3ByYWN0L21haW4vZG90bmV0LXppcHMvUFdBTElOS01BbmlmZXN0"
    "LnppcCJ9LCB7Im5hbWUiOiAiUFdBT2ZmbGluZVdvcmtzIiwgImFpbSI6ICJQV0EgZXhhbXBsZSBj"
    "b21iaW5pbmcgb2ZmbGluZSBzdXBwb3J0LCBhIG1hbmlmZXN0IGFuZCBhIHNlcnZpY2Ugd29ya2Vy"
    "LiIsICJzb2Z0d2FyZSI6ICJWaXN1YWwgU3R1ZGlvIC8gLk5FVCIsICJzdGVwcyI6ICJEb3dubG9h"
    "ZCB0aGUgemlwLCBleHRyYWN0IGl0LCB0aGVuIG9wZW4gdGhlIHNvbHV0aW9uIGZpbGUgaW5zaWRl"
    "IGluIFZpc3VhbCBTdHVkaW8uIiwgImZpbGVzIjogW10sICJydW4iOiAiRXh0cmFjdCB0aGUgemlw"
    "IGFuZCBvcGVuIHRoZSBzb2x1dGlvbiBpbiBWaXN1YWwgU3R1ZGlvLCB0aGVuIHJ1biB0aGUgcHJv"
    "amVjdC4iLCAiZG93bmxvYWQiOiAiaHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL3By"
    "YXNoYW50c2hpcmsvcHJhY3QvbWFpbi9kb3RuZXQtemlwcy9QV0FPZmZsaW5lV29ya3MuemlwIn0s"
    "IHsibmFtZSI6ICJQcmFjdGljYWw5IiwgImFpbSI6ICJBU1AuTkVUIENvcmUgQVBJIHdpdGggYSBT"
    "dHVkZW50cyBjb250cm9sbGVyIGFuZCBhbiBFbnRpdHkgRnJhbWV3b3JrIENvcmUgZGF0YWJhc2Ug"
    "Y29udGV4dCwgaW5jbHVkaW5nIG1pZ3JhdGlvbnMuIiwgInNvZnR3YXJlIjogIlZpc3VhbCBTdHVk"
    "aW8gLyAuTkVUIiwgInN0ZXBzIjogIkRvd25sb2FkIHRoZSB6aXAsIGV4dHJhY3QgaXQsIHRoZW4g"
    "b3BlbiB0aGUgc29sdXRpb24gZmlsZSBpbnNpZGUgaW4gVmlzdWFsIFN0dWRpby4iLCAiZmlsZXMi"
    "OiBbXSwgInJ1biI6ICJFeHRyYWN0IHRoZSB6aXAgYW5kIG9wZW4gdGhlIHNvbHV0aW9uIGluIFZp"
    "c3VhbCBTdHVkaW8sIHRoZW4gcnVuIHRoZSBwcm9qZWN0LiIsICJkb3dubG9hZCI6ICJodHRwczov"
    "L3Jhdy5naXRodWJ1c2VyY29udGVudC5jb20vcHJhc2hhbnRzaGlyay9wcmFjdC9tYWluL2RvdG5l"
    "dC16aXBzL1ByYWN0aWNhbDkuemlwIn0sIHsibmFtZSI6ICJQcm9kdWN0RUZDb3JlIiwgImFpbSI6"
    "ICJBU1AuTkVUIGFwcCB1c2luZyBFbnRpdHkgRnJhbWV3b3JrIENvcmUgZm9yIHByb2R1Y3QgZGF0"
    "YS4iLCAic29mdHdhcmUiOiAiVmlzdWFsIFN0dWRpbyAvIC5ORVQiLCAic3RlcHMiOiAiRG93bmxv"
    "YWQgdGhlIHppcCwgZXh0cmFjdCBpdCwgdGhlbiBvcGVuIHRoZSBzb2x1dGlvbiBmaWxlIGluc2lk"
    "ZSBpbiBWaXN1YWwgU3R1ZGlvLiIsICJmaWxlcyI6IFtdLCAicnVuIjogIkV4dHJhY3QgdGhlIHpp"
    "cCBhbmQgb3BlbiB0aGUgc29sdXRpb24gaW4gVmlzdWFsIFN0dWRpbywgdGhlbiBydW4gdGhlIHBy"
    "b2plY3QuIiwgImRvd25sb2FkIjogImh0dHBzOi8vcmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbS9w"
    "cmFzaGFudHNoaXJrL3ByYWN0L21haW4vZG90bmV0LXppcHMvUHJvZHVjdEVGQ29yZS56aXAifSwg"
    "eyJuYW1lIjogIlB1c2hOb3RpZmljYXRpb24iLCAiYWltIjogIkFTUC5ORVQgYXBwIHdpdGggYSBQ"
    "V0EgcHVzaCBub3RpZmljYXRpb24gZnJvbnQtZW5kLCBpbmNsdWRpbmcgYSBtYW5pZmVzdCBhbmQg"
    "c2VydmljZSB3b3JrZXIuIiwgInNvZnR3YXJlIjogIlZpc3VhbCBTdHVkaW8gLyAuTkVUIiwgInN0"
    "ZXBzIjogIkRvd25sb2FkIHRoZSB6aXAsIGV4dHJhY3QgaXQsIHRoZW4gb3BlbiB0aGUgc29sdXRp"
    "b24gZmlsZSBpbnNpZGUgaW4gVmlzdWFsIFN0dWRpby4iLCAiZmlsZXMiOiBbXSwgInJ1biI6ICJF"
    "eHRyYWN0IHRoZSB6aXAgYW5kIG9wZW4gdGhlIHNvbHV0aW9uIGluIFZpc3VhbCBTdHVkaW8sIHRo"
    "ZW4gcnVuIHRoZSBwcm9qZWN0LiIsICJkb3dubG9hZCI6ICJodHRwczovL3Jhdy5naXRodWJ1c2Vy"
    "Y29udGVudC5jb20vcHJhc2hhbnRzaGlyay9wcmFjdC9tYWluL2RvdG5ldC16aXBzL1B1c2hOb3Rp"
    "ZmljYXRpb24uemlwIn0sIHsibmFtZSI6ICJTb3J0ZWRDaXRpZXMiLCAiYWltIjogIkNvbnNvbGUg"
    "YXBwIHRoYXQgcmVhZHMgMTAgY2l0eSBuYW1lcywgc29ydHMgdGhlbSwgYW5kIHByaW50cyB0aGUg"
    "c29ydGVkIGxpc3QuIiwgInNvZnR3YXJlIjogIlZpc3VhbCBTdHVkaW8gLyAuTkVUIiwgInN0ZXBz"
    "IjogIkRvd25sb2FkIHRoZSB6aXAsIGV4dHJhY3QgaXQsIHRoZW4gb3BlbiB0aGUgc29sdXRpb24g"
    "ZmlsZSBpbnNpZGUgaW4gVmlzdWFsIFN0dWRpby4iLCAiZmlsZXMiOiBbXSwgInJ1biI6ICJFeHRy"
    "YWN0IHRoZSB6aXAgYW5kIG9wZW4gdGhlIHNvbHV0aW9uIGluIFZpc3VhbCBTdHVkaW8sIHRoZW4g"
    "cnVuIHRoZSBwcm9qZWN0LiIsICJkb3dubG9hZCI6ICJodHRwczovL3Jhdy5naXRodWJ1c2VyY29u"
    "dGVudC5jb20vcHJhc2hhbnRzaGlyay9wcmFjdC9tYWluL2RvdG5ldC16aXBzL1NvcnRlZENpdGll"
    "cy56aXAifSwgeyJuYW1lIjogIlN0dWRlbnRBUEkiLCAiYWltIjogIkFTUC5ORVQgQ29yZSBXZWIg"
    "QVBJIGZvciBzdHVkZW50IHJlY29yZHMuIiwgInNvZnR3YXJlIjogIlZpc3VhbCBTdHVkaW8gLyAu"
    "TkVUIiwgInN0ZXBzIjogIkRvd25sb2FkIHRoZSB6aXAsIGV4dHJhY3QgaXQsIHRoZW4gb3BlbiB0"
    "aGUgc29sdXRpb24gZmlsZSBpbnNpZGUgaW4gVmlzdWFsIFN0dWRpby4iLCAiZmlsZXMiOiBbXSwg"
    "InJ1biI6ICJFeHRyYWN0IHRoZSB6aXAgYW5kIG9wZW4gdGhlIHNvbHV0aW9uIGluIFZpc3VhbCBT"
    "dHVkaW8sIHRoZW4gcnVuIHRoZSBwcm9qZWN0LiIsICJkb3dubG9hZCI6ICJodHRwczovL3Jhdy5n"
    "aXRodWJ1c2VyY29udGVudC5jb20vcHJhc2hhbnRzaGlyay9wcmFjdC9tYWluL2RvdG5ldC16aXBz"
    "L1N0dWRlbnRBUEkuemlwIn0sIHsibmFtZSI6ICJWYWxpZGF0aW9ucyIsICJhaW0iOiAiQVNQLk5F"
    "VCBXZWIgRm9ybXMgYXBwIHNob3dpbmcgZm9ybSB2YWxpZGF0aW9uLiIsICJzb2Z0d2FyZSI6ICJW"
    "aXN1YWwgU3R1ZGlvIC8gLk5FVCIsICJzdGVwcyI6ICJEb3dubG9hZCB0aGUgemlwLCBleHRyYWN0"
    "IGl0LCB0aGVuIG9wZW4gdGhlIHNvbHV0aW9uIGZpbGUgaW5zaWRlIGluIFZpc3VhbCBTdHVkaW8u"
    "IiwgImZpbGVzIjogW10sICJydW4iOiAiRXh0cmFjdCB0aGUgemlwIGFuZCBvcGVuIHRoZSBzb2x1"
    "dGlvbiBpbiBWaXN1YWwgU3R1ZGlvLCB0aGVuIHJ1biB0aGUgcHJvamVjdC4iLCAiZG93bmxvYWQi"
    "OiAiaHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL3ByYXNoYW50c2hpcmsvcHJhY3Qv"
    "bWFpbi9kb3RuZXQtemlwcy9WYWxpZGF0aW9ucy56aXAifSwgeyJuYW1lIjogImNhbGMiLCAiYWlt"
    "IjogIkFTUC5ORVQgTVZDIGNhbGN1bGF0b3IgYXBwLiIsICJzb2Z0d2FyZSI6ICJWaXN1YWwgU3R1"
    "ZGlvIC8gLk5FVCIsICJzdGVwcyI6ICJEb3dubG9hZCB0aGUgemlwLCBleHRyYWN0IGl0LCB0aGVu"
    "IG9wZW4gdGhlIHNvbHV0aW9uIGZpbGUgaW5zaWRlIGluIFZpc3VhbCBTdHVkaW8uIiwgImZpbGVz"
    "IjogW10sICJydW4iOiAiRXh0cmFjdCB0aGUgemlwIGFuZCBvcGVuIHRoZSBzb2x1dGlvbiBpbiBW"
    "aXN1YWwgU3R1ZGlvLCB0aGVuIHJ1biB0aGUgcHJvamVjdC4iLCAiZG93bmxvYWQiOiAiaHR0cHM6"
    "Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL3ByYXNoYW50c2hpcmsvcHJhY3QvbWFpbi9kb3Ru"
    "ZXQtemlwcy9jYWxjLnppcCJ9XX1d"
)).decode("utf-8"))

SEP = "# " + "=" * 70


def build_plain():
    out = []
    for section in SECTIONS:
        out.append(SEP)
        out.append("# " + section["title"])
        out.append(SEP)
        out.append("")
        for it in section["items"]:
            out.append(SEP)
            out.append("# " + it["name"])
            out.append(SEP)
            out.append("Aim: " + it["aim"])
            out.append("")
            out.append("Software: " + it["software"])
            out.append("")
            out.append("Steps: " + it["steps"])
            out.append("")
            for f in it["files"]:
                out.append("File: " + f["filename"])
                out.append("Where: " + f["where"])
                out.append("How: " + f["how"])
                out.append(f["code"].rstrip())
                out.append("")
            out.append("Run: " + it["run"])
            if it.get("download"):
                out.append("Download: " + it["download"])
            out.append("")
            out.append("")
    return "\n".join(out).rstrip() + "\n"


def build_html():
    sections_json = json.dumps(SECTIONS, ensure_ascii=False).replace("</", "<\\/")
    return PAGE.replace("__SECTIONS_JSON__", sections_json)


PAGE = '<!DOCTYPE html>\n<html lang="en"><head><meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1">\n<title>Pract | .NET Practicals</title>\n<style>\n:root{--bg:#e9e9e7;--panel:#f6f6f4;--panel2:#ececea;--border:#d5d5d2;--text:#3d3d3d;--muted:#7d7d7d;--accent:#5c5c5c;--hover:#e2e2df;--active:#dfdfdc;--codebg:#efefed;--inputbg:#f6f6f4;color-scheme:light}\n[data-theme="dark"]{--bg:#1c1c1c;--panel:#242424;--panel2:#2a2a2a;--border:#353535;--text:#bcbcbc;--muted:#888888;--accent:#a2a2a2;--hover:#2e2e2e;--active:#2b2b2b;--codebg:#1f1f1f;--inputbg:#242424;color-scheme:dark}\n*{box-sizing:border-box}\nbody{margin:0;height:100vh;display:flex;gap:16px;padding:16px;background:var(--bg);color:var(--text);\n     font-family:\'Inter\',-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif;font-size:16px;line-height:1.55}\n::-webkit-scrollbar{width:9px;height:9px}\n::-webkit-scrollbar-track{background:var(--panel)}\n::-webkit-scrollbar-thumb{background:#b0b0b0;border-radius:5px}\n::-webkit-scrollbar-thumb:hover{background:#9a9a9a}\nbutton,input{font:inherit}\nbutton:focus-visible,input:focus-visible{outline:2px solid #888888;outline-offset:2px}\n.sidebar{width:32%;max-width:380px;min-width:260px;background:var(--panel);border:1px solid var(--border);border-radius:12px;\n         padding:14px;display:flex;flex-direction:column;min-height:0}\n.sidebar h2{margin:0 0 10px;font-size:1rem;color:var(--muted);font-weight:600;letter-spacing:.3px;\n            border-bottom:1px solid var(--border);padding-bottom:10px}\n.searchrow{margin-bottom:8px}\n.searchrow input{width:100%;padding:10px 12px;border:1px solid var(--border);border-radius:8px;\n                 background:var(--inputbg);color:var(--text)}\n.searchrow input::placeholder{color:var(--muted)}\n.section-actions{display:flex;gap:8px;margin-bottom:10px}\n.section-actions button{flex:1;padding:7px 8px;border:1px solid var(--border);border-radius:8px;\n                        background:var(--panel2);color:var(--text);font-size:.85rem;cursor:pointer}\n.section-actions button:hover{background:var(--hover);color:var(--text);border-color:var(--border)}\n.section-button{text-align:left;width:100%;padding:11px 12px;border:none;border-radius:8px;background:var(--panel2);\n             color:var(--text);font-size:.95rem;font-weight:600;cursor:pointer}\n.section-button:hover{background:var(--hover);color:var(--text)}\n.section-list{display:flex;flex-direction:column;gap:4px;padding:2px 0 10px 8px}\n.section-list.hidden{display:none}\n.list{overflow-y:auto;display:flex;flex-direction:column;gap:4px;padding-right:4px}\n.file-button{text-align:left;width:100%;padding:11px 12px;border:none;border-left:3px solid transparent;border-radius:8px;background:transparent;\n             color:var(--text);font-size:.92rem;line-height:1.4;cursor:pointer;transition:background .12s,color .12s}\n.file-button:hover{background:var(--hover);color:var(--text)}\n.file-button.active{background:var(--active);color:var(--text);font-weight:600;border-left-color:var(--accent)}\n.hint{margin:10px 0 0;color:var(--muted);font-size:.85rem;line-height:1.45}\n.noresults{padding:12px;color:var(--text);font-size:.92rem}\n.hidden{display:none}\n.viewer{flex:1 1 auto;background:var(--panel);border:1px solid var(--border);border-radius:12px;\n        padding:16px 18px;display:flex;flex-direction:column;min-height:0;min-width:0}\n.topbar{display:flex;align-items:flex-start;justify-content:space-between;gap:16px;flex-wrap:wrap;\n        border-bottom:1px solid var(--border);padding-bottom:12px;margin-bottom:12px}\n.topbar h1{margin:0;font-size:1.2rem;line-height:1.3;color:var(--accent);font-weight:600}\n.progress{margin-top:4px;color:var(--muted);font-size:.88rem}\n.pager{display:flex;gap:8px;flex-shrink:0}\n.pager button{padding:9px 14px;border:1px solid var(--border);border-radius:10px;background:var(--panel2);color:var(--text);\n              font-size:.9rem;font-weight:600;cursor:pointer;white-space:nowrap}\n.pager button:hover:not(:disabled){background:var(--hover);border-color:var(--border);color:var(--text)}\n.pager button:disabled{opacity:.45;cursor:default}\n.viewbody{flex:1 1 auto;overflow:auto;min-height:0}\n.meta{margin-bottom:16px;line-height:1.65;font-size:1rem;color:var(--text);white-space:pre-wrap;max-width:74ch}\n.meta p{margin:0 0 12px}\n.fileblock{margin-bottom:18px;background:var(--panel2);border:1px solid var(--border);border-radius:10px;padding:14px}\n.filehead{display:flex;align-items:center;justify-content:space-between;gap:12px;flex-wrap:wrap;margin-bottom:8px}\n.filename{font-family:\'Fira Code\',Consolas,Menlo,monospace;font-size:.95rem;color:var(--accent);font-weight:600;word-break:break-all}\n.filemeta{font-size:.92rem;line-height:1.55;color:var(--text);margin-bottom:10px;white-space:pre-wrap}\n.copy{cursor:pointer;border:none;border-radius:10px;background:#777777;color:#fff;font-size:.9rem;\n      font-weight:600;padding:9px 18px;white-space:nowrap;transition:background .15s,transform .05s}\n.copy:hover{background:#666666}\n.copy:active{transform:scale(.97)}\n.copy.ok{background:#7a7a7a}\n.codewrap{background:var(--codebg);border-radius:10px;padding:16px;overflow:auto}\n.fileblock .codewrap{background:#0000;border:1px solid var(--border)}\npre{margin:0}\ncode{font-family:\'Fira Code\',Consolas,Menlo,monospace;font-size:.95rem;line-height:1.6;color:var(--text);white-space:pre}\n.run{margin-top:4px;line-height:1.6;font-size:.98rem;color:var(--text);white-space:pre-wrap;max-width:74ch}\n@media(max-width:760px){body{flex-direction:column;height:auto}.sidebar{width:auto;max-width:none;max-height:46vh}\n  .viewer{min-height:60vh}.topbar h1{font-size:1.2rem}}\n</style></head>\n<body>\n<nav class="sidebar"><h2>Practs</h2>\n<div class="searchrow"><input id="search" type="search" placeholder="Search practicals, for example ssh or tar" aria-label="Search practicals"></div>\n<div class="section-actions"><button id="expandAll" type="button">Expand all</button><button id="collapseAll" type="button">Collapse all</button></div>\n<div id="sections" class="list"></div><div id="noresults" class="noresults hidden">No entries match that search.</div>\n<p class="hint">Tip: use the Previous and Next buttons, or the left and right arrow keys, to move through the practicals in order.</p></nav>\n<section class="viewer">\n  <div class="topbar"><div><h1 id="name">Select a pract</h1><div id="progress" class="progress"></div></div>\n  <div class="pager"><button id="themeBtn" type="button">Dark mode</button><button id="prevBtn" type="button">Previous</button><button id="nextBtn" type="button">Next</button></div></div>\n  <div class="viewbody"><div class="meta" id="meta"></div><div id="files"></div><div class="run" id="run"></div></div>\n</section>\n<script>\nconst SECTIONS = __SECTIONS_JSON__;\nconst themeBtn=document.getElementById("themeBtn");\nfunction applyTheme(t){document.documentElement.dataset.theme=t;themeBtn.textContent=t==="dark"?"Light mode":"Dark mode";try{localStorage.setItem("pract-theme",t);}catch(e){}}\nlet savedTheme=null;try{savedTheme=localStorage.getItem("pract-theme");}catch(e){}\napplyTheme(savedTheme==="dark"||savedTheme==="light"?savedTheme:"light");\nthemeBtn.onclick=()=>applyTheme(document.documentElement.dataset.theme==="dark"?"light":"dark");\nconst FILES = SECTIONS.flatMap(s=>s.items);\nconst sectionsEl=document.getElementById("sections"),nameEl=document.getElementById("name"),\n      metaEl=document.getElementById("meta"),filesEl=document.getElementById("files"),runEl=document.getElementById("run"),\n      progressEl=document.getElementById("progress"),prevBtn=document.getElementById("prevBtn"),\n      nextBtn=document.getElementById("nextBtn"),searchEl=document.getElementById("search"),\n      noresultsEl=document.getElementById("noresults");\nlet current=0;\nconst sectionHeads=[];\nfunction para(parent,label,text){if(!text)return;const p=document.createElement("p");p.textContent=label+text;parent.appendChild(p);}\nfunction doCopy(text,btn){const orig=btn.textContent;const done=()=>{btn.textContent="Copied!";btn.classList.add("ok");setTimeout(()=>{btn.textContent=orig;btn.classList.remove("ok");},1400);};\n  if(navigator.clipboard&&window.isSecureContext){navigator.clipboard.writeText(text).then(done,()=>fb(text,done));}else{fb(text,done);}}\nfunction fb(text,done){const ta=document.createElement("textarea");ta.value=text;ta.style.position="fixed";ta.style.opacity="0";\n  document.body.appendChild(ta);ta.focus();ta.select();try{document.execCommand("copy");done();}catch(e){alert("Copy failed, select manually.");}document.body.removeChild(ta);}\nfunction setSectionOpen(si,open){const h=sectionHeads[si];const div=h.nextDiv;div.classList.toggle("hidden",!open);\n  h.el.textContent=(open?"\\u25be ":"\\u25b8 ")+SECTIONS[si].title+" ("+SECTIONS[si].items.length+")";\n  h.el.setAttribute("aria-expanded",open?"true":"false");}\nfunction show(i){if(i<0)i=0;if(i>=FILES.length)i=FILES.length-1;current=i;const e=FILES[i];\n  nameEl.textContent=e.name;metaEl.textContent="";filesEl.textContent="";runEl.textContent="";\n  progressEl.textContent=(i+1)+" of "+FILES.length;\n  prevBtn.disabled=i===0;nextBtn.disabled=i===FILES.length-1;\n  para(metaEl,"Aim: ",e.aim);para(metaEl,"Software: ",e.software);para(metaEl,"Steps: ",e.steps);if(e.download){const p=document.createElement("p");const a=document.createElement("a");a.className="copy";a.href=e.download;a.textContent="Download zip";a.style.textDecoration="none";a.style.display="inline-block";p.appendChild(a);metaEl.appendChild(p);}\n  e.files.forEach(f=>{const b=document.createElement("div");b.className="fileblock";\n    const h=document.createElement("div");h.className="filehead";\n    const fn=document.createElement("span");fn.className="filename";fn.textContent=f.filename;h.appendChild(fn);\n    const btn=document.createElement("button");btn.className="copy";btn.textContent="Copy "+f.filename;\n    btn.onclick=()=>doCopy(f.code,btn);h.appendChild(btn);b.appendChild(h);\n    const m=document.createElement("div");m.className="filemeta";m.textContent="Where: "+f.where+"\\nHow: "+f.how;b.appendChild(m);\n    const w=document.createElement("div");w.className="codewrap";const pre=document.createElement("pre");\n    const code=document.createElement("code");code.textContent=f.code;pre.appendChild(code);w.appendChild(pre);b.appendChild(w);\n    filesEl.appendChild(b);});\n  para(runEl,"Run: ",e.run);\n  document.querySelectorAll(".file-button").forEach((b,j)=>b.classList.toggle("active",j===i));\n  const activeBtn=document.querySelectorAll(".file-button")[i];\n  if(activeBtn){activeBtn.scrollIntoView({block:"nearest"});\n    const si=SECTIONS.findIndex(s=>s.items.indexOf(e)>=0);\n    if(si>=0)setSectionOpen(si,true);}\n  document.querySelector(".viewbody").scrollTop=0;}\nprevBtn.onclick=()=>show(current-1);\nnextBtn.onclick=()=>show(current+1);\ndocument.addEventListener("keydown",ev=>{if(ev.target===searchEl)return;\n  if(ev.key==="ArrowLeft")show(current-1);if(ev.key==="ArrowRight")show(current+1);});\nlet gi=0;\nSECTIONS.forEach((s,si)=>{const h=document.createElement("button");h.className="section-button";\n  h.textContent=(si===0?"\\u25be ":"\\u25b8 ")+s.title+" ("+s.items.length+")";\n  h.setAttribute("aria-expanded",si===0?"true":"false");\n  const div=document.createElement("div");div.className="section-list"+(si===0?"":" hidden");\n  h.onclick=()=>{const hid=div.classList.toggle("hidden");\n    h.textContent=(hid?"\\u25b8 ":"\\u25be ")+s.title+" ("+s.items.length+")";\n    h.setAttribute("aria-expanded",hid?"false":"true");};\n  sectionHeads.push({el:h,nextDiv:div});\n  sectionsEl.appendChild(h);sectionsEl.appendChild(div);\n  s.items.forEach(f=>{const b=document.createElement("button");b.className="file-button";b.textContent=f.name;\n    b.dataset.search=(f.name+" "+(f.aim||"")).toLowerCase();\n    const idx=gi++;b.onclick=()=>show(idx);div.appendChild(b);});});\nfunction applySearch(){const q=searchEl.value.trim().toLowerCase();let shown=0;\n  sectionHeads.forEach((h,si)=>{const div=h.nextDiv;let count=0;\n    div.querySelectorAll(".file-button").forEach(b=>{const ok=!q||b.dataset.search.includes(q);\n      b.style.display=ok?"":"none";if(ok)count++;});\n    const showSection=count>0;h.el.style.display=showSection?"":"none";div.style.display=showSection?"":"none";\n    if(q&&showSection)div.classList.remove("hidden");if(!q)div.classList.toggle("hidden",si!==0);\n    if(!q)h.el.textContent=(si===0?"\\u25be ":"\\u25b8 ")+SECTIONS[si].title+" ("+SECTIONS[si].items.length+")";\n    shown+=count;});\n  noresultsEl.classList.toggle("hidden",shown>0);}\nsearchEl.addEventListener("input",applySearch);\ndocument.getElementById("expandAll").onclick=()=>sectionHeads.forEach((h,si)=>setSectionOpen(si,true));\ndocument.getElementById("collapseAll").onclick=()=>sectionHeads.forEach((h,si)=>setSectionOpen(si,false));\nif(FILES.length)show(0);\n</script>\n</body></html>\n'


# ----- Local dev server:  python server.py [port] -----
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer


def _wants_raw(ua, accept, path):
    ua, accept = ua.lower(), accept.lower()
    if path in ("/raw", "/plain", "/code"):
        return True
    if any(x in ua for x in ("curl", "wget", "httpie", "python-requests",
                             "powershell", "windowspowershell", "webrequest")):
        return True
    return "text/html" not in accept and accept and accept != "*/*"


class _H(BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path.split("?")[0].rstrip("/")
        raw = _wants_raw(self.headers.get("User-Agent", ""), self.headers.get("Accept", ""), path)
        body = build_plain() if raw else build_html()
        ctype = "text/plain; charset=utf-8" if raw else "text/html; charset=utf-8"
        data = body.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def log_message(self, *a):
        pass


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    print("Browser : http://localhost:%d" % port)
    print("Terminal: curl.exe http://localhost:%d   (or  irm http://localhost:%d )" % (port, port))
    try:
        HTTPServer(("0.0.0.0", port), _H).serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")
