class PreEmphasizer(object):
    @classmethod
    def processBuffer(cls, buf):
        preEnergy = buf.energy()

        alpha = cls.alpha()
        unmodifiedPreviousSample = buf.samples[0]
        tempSample = None

        first_sample = buf.samples[0]
        buf.samples = buf.samples[1:] + (buf.samples[:-1] * alpha)
        buf.samples = sp.insert(buf.samples, 0, first_sample)

        cls.scaleBuffer(buf, preEnergy, buf.energy())

    @classmethod
    def alpha(cls):
        return settings.preEmphasisAlpha

    @classmethod
    def scaleBuffer(cls, buf, preEnergy, postEnergy):
        scale = sp.sqrt(preEnergy / postEnergy)

        buf.samples *= scale


