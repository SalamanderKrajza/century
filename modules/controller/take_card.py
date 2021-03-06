from PyQt5.QtWidgets import QPushButton, QLabel
from PyQt5 import QtCore, QtGui, QtWidgets
from modules.view.img import img
from modules.view.Popup import Popup


def check_if_popup_needed(popup_type, distance_to_right_edge=99):
    if popup_type == 'Harvest':
        #Harvest cards don't have not any requirements to play
        return False
    if popup_type == 'PlayableStore':
        #If we're buying Playable card we need to check how close it is to end of the list
        if not distance_to_right_edge:
            return False
    if popup_type == 'too_much_resources':
        return True

    return True

def press_the_card(ClickedWholeWidget, ClickedCardWidget, Ui, Game, Popup, event):
    """Defines which actions should happened when card is pressed"""

    #If status is "USED" we shouldn't be able to press it untill player rest
    if ClickedCardWidget.Card.used == True:
        return

    #The parents of Whole Widget are ClickedCardWidget->ClickedWholeWidget->V/HBoxLayout->ScrollAreaWidgetContents->ScrollArea
    SourceScrollBox = ClickedWholeWidget.parent().parent().parent().objectName()
    if SourceScrollBox == 'PlayableStore-ScrollArea':
        popup_type = 'PlayableStore'
    elif SourceScrollBox == 'BuyableStore-ScrollArea': 
        popup_type = 'BuyableStore'
    elif SourceScrollBox == 'PlayerHand-ScrollArea': 
        popup_type = ClickedCardWidget.Card.card_type
    else:
        popup_type = 'unknown'

    ClickedCardWidget.Card.popup_type = popup_type

    Player = Game.CurrentPlayer
    
    #In case Player press another card while popup is visible
    Popup.close_popup()

    Popup.configure_popup(popup_type=popup_type, ClickedCardWidget=ClickedCardWidget)

    if check_if_popup_needed(popup_type=popup_type, distance_to_right_edge=Popup.distance_to_right_edge):
        #Show popup
        Popup.display_popup()
    else:
        Popup.action_confirmed(ClickedWholeWidget, ClickedCardWidget, Ui, Game)
        pass

    #Next steps should depends on what happened on popup



