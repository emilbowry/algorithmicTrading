#include "tools\index.mqh "
#include "config\index.mqh"

struct AgentTradeRequest : MqlTradeRequest
{
   // this.symbol = SYMBOL;
};

class tradeAgent : public CTrade
{

private:
   AgentTradeRequest myAgentRequest;
   MqlTradeResult myResult;
   CPositionInfo myPositionInfo;
   ulong myId; // add hashed

public:
   void Initialise();
   void InitialiseRequest(AgentTradeRequest &aReq);

   bool isPositionClosed();
   bool isOrderSubmitted();
   bool isPositionOpen();
   bool isGoodDealPlaced();
   bool isNoTradeYet();

   tradeAgent(ulong id)
   {
      myId = id;
   }
};

void tradeAgent::Initialise()
{
   //  this.isPositionClosed() = false;
   //  this.isOrderSubmitted() = false;
   //  this.isPositionOpen() = false;
   //  this.isGoodDealPlaced() = false;

   // FIX THIS
}
void tradeAgent::InitialiseRequest(AgentTradeRequest &aReq)
{
   this.myAgentRequest = aReq;

   // add additional request logic
}

bool tradeAgent::isNoTradeYet()
{

   return (isPositionClosed() || isPositionOpen());
}

bool tradeAgent::isPositionClosed()
{
   {
      if (this.myPositionInfo.Select(SYMBOL))
      {

         if (!this.PositionClose(this.myPositionInfo.Ticket()))
         {
            Alert("PositionClose error %d", GetLastError());
            return false;
         }
         Alert("PositionClosed");

         return true;
      }
   }
   return false;
}

bool tradeAgent::isOrderSubmitted()
{

   this.InitialiseRequest(this.myAgentRequest);
   if (!this.OrderSend(this.myAgentRequest, this.myResult))
   {
      return false;
   }
   return true;
}

bool tradeAgent::isGoodDealPlaced()
{
   if (OrderSelect(this.RequestOrder()))
   {
      if (OrderGetInteger(ORDER_TICKET) == 0)
      {
         return false;
      }
      if ((OrderGetInteger(ORDER_TICKET) == ORDER_STATE_EXPIRED) || (OrderGetInteger(ORDER_TICKET) == ORDER_STATE_REJECTED) || (OrderGetInteger(ORDER_TICKET) == ORDER_STATE_CANCELED))
      {
         return false;
      }
      return true;
   }
   return false; // check logic on this
}

bool tradeAgent::isPositionOpen()
{
   return (!(PositionsTotal() == 0));
}