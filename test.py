from asyncflows import AsyncFlows


async def main():
    role = "Biotechnological Nurse"
    resume_text = "Highly motivated and detail-oriented Biotech Nurse with [Number] years of experience in [Specific areas of expertise within biotech nursing, e.g., cell culture, bioprocessing, clinical trials]. Skilled in [List of relevant skills, e.g., aseptic techniques, sterile processing, equipment calibration, data analysis]. Passionate about [Mention your passion related to the field, e.g., advancing biotechnology research, contributing to innovative therapies]."
    job_description = "Dealing with machines as I am qualified in Biotechnology"
    name = "Robert"
    hiring_manager ="Kelvin"
    referral ="Internet Ad"
    company= "Huts Co."
    cand_address = 84515
    comp_address = 254
    flow = AsyncFlows.from_file("main.yaml").set_vars(
        role = role,
        resume_text = resume_text,
        job_description = job_description,
        name = name,
        hiring_manager = hiring_manager,
        referral = referral,
        company = company,
        cand_address = cand_address,
        comp_address = comp_address
    )


    result = await flow.run()
    print(result)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())