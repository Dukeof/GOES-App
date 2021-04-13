import styled from 'styled-components';
import { BlueButton } from "../../../globalstyles/globalStyle"

export const RegistrationWrapper = styled.div`
    width: 100%;
    height: 50%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    color: #FFFFFF;
    font-size: 24px;
`;

export const RegInputContainer = styled.div`
    display: flex;
    align-items: flex-start;
    flex-direction: column;
    justify-content: center;
`;

export const RegButton = styled(BlueButton)`
    margin-top: 1.5rem;
    outline:transparent;

`;