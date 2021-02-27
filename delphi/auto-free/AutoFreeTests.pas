unit AutoFreeTests;

interface

uses
  TestFramework, Classes;

type
  TestAutoFree = class(TTestCase)
  public
    procedure SetUp; override;
    procedure TearDown; override;
  published
    procedure TestAutoFreeObject;
  end;

  TClasseTeste = class
  end;

implementation

uses
  AutoFree;

procedure TestAutoFree.SetUp;
begin
end;

procedure TestAutoFree.TearDown;
begin
end;

procedure TestAutoFree.TestAutoFreeObject;
var
  Obj1: TClasseTeste;
  Obj2: TClasseTeste;
begin
  Obj1 := TClasseTeste.Create;
  TAutoFree<TClasseTeste>.Add(Obj1);
  Obj2 := TClasseTeste.Create;
  TAutoFree<TClasseTeste>.Add(Obj2);
  //ReportMemoryLeaksOnShutdown
end;

initialization
  RegisterTest(TestAutoFree.Suite);
end.

