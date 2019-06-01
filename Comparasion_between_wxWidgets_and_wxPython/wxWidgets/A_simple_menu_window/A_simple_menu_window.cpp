//----------------------------------------------------------------------------
// Purpose: a simple menu window, using wxWidgets.
// Date: 2017-01-25
//----------------------------------------------------------------------------

#include <wx/wx.h>

class App : public wxApp
{
    virtual bool OnInit();
};

class Frame : public wxFrame
{
public:
    Frame(const wxString & title, const wxPoint & pos, const wxSize & size);
    void OnQuit(wxCommandEvent & event);
    void OnAbout(wxCommandEvent & event);
    DECLARE_EVENT_TABLE()
};

enum
{
    ID_Quit = 1,
    ID_About,
};

BEGIN_EVENT_TABLE(Frame, wxFrame)
    EVT_MENU(ID_Quit, Frame::OnQuit)
    EVT_MENU(ID_About, Frame::OnAbout)
END_EVENT_TABLE()

IMPLEMENT_APP(App)

bool App::OnInit()
{
    Frame *frame = new Frame("Hello World", wxPoint(50, 50), wxSize(450, 340));
    frame->Show(TRUE);
    SetTopWindow(frame);
    return TRUE;
}

Frame::Frame(const wxString & title, const wxPoint & pos, const wxSize & size):
    wxFrame((wxFrame *)NULL, -1, title, pos, size)
{
    wxMenu *menuFile = new wxMenu;
    menuFile->Append(ID_About, "&About...");
    menuFile->AppendSeparator();
    menuFile->Append(ID_Quit, "E&xit");

    wxMenuBar *menuBar = new wxMenuBar;
    menuBar->Append(menuFile, "&File");
    SetMenuBar(menuBar);

    CreateStatusBar();
    SetStatusText("Welcome to wxWidgets!");
}

void Frame::OnQuit(wxCommandEvent & WXUNUSED(event))
{
    Close(TRUE);
}

void Frame::OnAbout(wxCommandEvent & WXUNUSED(event))
{
    wxMessageBox("This is a wxWidgets Hello world sample", "About Hello World",
                 wxOK | wxICON_INFORMATION, this);
}

