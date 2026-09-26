# APC interview guide — 2 minute demonstration

## Purpose

This repository is designed to support a concise discussion of valuation judgement, not to turn an APC interview into a software demonstration.

## Suggested 2-minute explanation

> I developed this public project to deepen my understanding of growth-explicit discounted cash flow valuation and to test how transparent modelling can support professional judgement. I used only public property information and clearly separated observed evidence from my modelling assumptions.
>
> The project progresses from straightforward investments to more complex multi-let and reversionary cases. At tenancy level I can model passing rent, ERV, lease expiry or break, voids, incentives, reletting costs and rental growth. The model then discounts the explicit cash flows and terminal value to present value.
>
> I also compare the DCF with traditional growth-implicit investment techniques and run sensitivity analysis around key assumptions such as the discount rate and exit yield. I did this because a DCF can create false precision if the inputs are weak.
>
> Most importantly, I would not treat the calculated output as the valuation conclusion. For Market Value I would need market-derived inputs, verified evidence and reconciliation against transactions. The model calculates; the valuer concludes.

## Be ready for these assessor questions

1. **Why did you choose DCF?**  
   Explain that it is particularly useful where cash flows are irregular or complex, while method/model selection remains a matter of professional judgement.

2. **What is the difference between an ARY and a DCF discount rate?**  
   An ARY is used in a growth-implicit capitalisation model; expected rental/capital growth is embedded in market pricing/yield. A growth-explicit DCF separately forecasts growth and discounts the resulting cash flows at a required return.

3. **How would you derive the discount rate?**  
   From market evidence and market-participant return requirements. Transaction analysis, where adequate data exist, is especially important. Do not invent a generic 'RICS rate'.

4. **How would you derive the exit yield?**  
   From market evidence, considering the expected asset quality, lease profile, age, location and market conditions at exit. Explain the relationship between the exit assumptions and the rest of the cash flow.

5. **Why run sensitivity analysis?**  
   To expose how the conclusion responds to uncertain inputs and avoid presenting a modelled figure with misleading precision.

6. **Market Value or Investment Value?**  
   Market Value requires market-participant assumptions. Investor-specific required returns, financing or strategic assumptions may produce Investment Value/worth instead.

7. **Why compare with a traditional investment method?**  
   It is a useful reasonableness check and demonstrates understanding of both growth-implicit and growth-explicit techniques.

8. **Would you rely on an asking price?**  
   No. Asking prices are contextual/marketing evidence. Completed transactions are generally stronger evidence of market price, subject to verification and comparability.

9. **What is the biggest risk in your model?**  
   Input quality. A technically correct DCF can still be a poor valuation if ERV, growth, discount rate, lease events, costs or exit assumptions are unsupported.

10. **Why publish the code?**  
    Transparency and auditability. It allows the calculation logic to be inspected and tested, while making clear that code does not replace valuation judgement.

## The line to remember

**A sophisticated model does not rescue weak evidence. My role as valuer is to interrogate the evidence, select appropriate assumptions, test the output and provide a reasoned conclusion.**
