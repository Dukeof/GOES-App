import styled from 'styled-components'
import { CenterContainer } from "../../globalstyles/globalStyle"

export const TitleWrapper = styled.div`
    width: 100%;
    height: 10%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    color: ${props => props.theme.labelcolor };
    font-size: 24px;
`;

export const PersonContainer = styled.div`
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    color: ${props => props.theme.labelcolor };
    line-height: 1.5;
`;
export const LeftContainer = styled.div`
    height: 100%;
    width: 50%;
    display: flex;
    flex-direction: column;
    justify-content: space-evenly;
    align-items: center;
    color: ${props => props.theme.labelcolor };
    border-right: 2px solid #30ADEA;
    label {
        font-size: 20px;
    }

`;
export const SupportContainer = styled.div`
    height: 50%;
    width: 50%;
    display: flex;
    flex-direction: column;
    justify-content: space-evenly;
    align-items: center;
    color: ${props => props.theme.labelcolor };
    font-size: 24px;

    a {
        font-size: 18px;
    }
`;
export const AboutContainer = styled(CenterContainer)`
    display: flex;
    flex-direction: row;
    justify-content: space-evenly;
`;

export const HyperLinks = styled.a`
    color: ${props => props.theme.labelcolor };
    text-decoration: none;
    :hover{
        color:#30ADEA;
    }
    :active{
        outline:transparent;
    }
    `