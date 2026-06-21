# Actionable Tips

1. **Treat mechanism disconfirmation as a stop signal.** When Tanya says email is separate from checkout/payment, pause before acting and ask what evidence would overturn that. Do not order a DNS or email revert unless you can name the causal path to payment failure.

2. **Rank log signals by symptom relevance, not volume.** The loudest errors are not always the cause. Use the question "which error sits on the critical path to zero successful transactions?" to keep PaymentService-style evidence above EmailService noise.

3. **Use failed actions to narrow, not scatter.** After a rollback or restart fails, write down what it rules out and what changed in the error. This will make your next move targeted instead of shifting to another broad fix like clearing caches or deleting certs.
